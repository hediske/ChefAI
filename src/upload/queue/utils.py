import os
import json
from lib.chroma_database import getChromaDB, getChromaDBOnCloud
from lib.chroma_store import ChromaStore
from langchain_core.documents import Document

def producer(filename, file_type, queue):
    """Modified to handle both recipe and non-recipe files"""
    try:
        if file_type == "recipe":
            # Special handling for recipe files
            with open(filename) as f:
                recipes_data = json.load(f)
            
            for recipe_id, recipe in recipes_data.items():
                # Create one document per recipe
                doc = {
                    "content": format_recipe_content(recipe),
                    "type": "full_recipe",
                    "recipe_id": recipe_id,
                    "title": recipe["title"],
                    "vegetarian": is_vegetarian(recipe["ingredients"]),
                    "picture_link": recipe.get("picture_link", "")
                }
                queue.put(([doc], filename, file_type))
                
        else:
            # Original handling for non-recipe files
            docs = prepareFile(file_path=filename, file_type=file_type)
            queue.put((docs, filename, file_type))
            
        print(f"Added file '{filename}' to queue")
        
    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

def consummer(queue, to_cloud=False):
    """Updated consumer to handle new recipe format"""
    client = ChromaStore(getChromaDBOnCloud() if to_cloud else getChromaDB())
    print(f"Process {os.getpid()} started")
    
    while True:
        try:
            batch = queue.get()
            if batch is None:  # Sentinel for shutdown
                break
                
            items, filename, file_type = batch
            
            # Convert all items to Document objects
            documents = []
            for item in items:
                if isinstance(item, dict):  # Recipe case
                    doc = Document(
                        page_content=item["content"],
                        metadata={k: v for k, v in item.items() if k != "content"}
                    )
                    documents.append(doc)
                else:  # Regular document case
                    documents.append(item)
            
            # Store documents
            client.add_documents(documents)
            print(f"Process {os.getpid()} added {len(documents)} items from {filename}")
            
        except Exception as e:
            print(f"Process {os.getpid()} failed: {str(e)}")

# Helper functions
def format_recipe_content(recipe):
    """Format recipe data into a string"""
    ingredients = [ing.replace("ADVERTISEMENT", "").strip() 
                  for ing in recipe["ingredients"] if ing.strip()]
    
    instructions = "\n".join(line.strip() 
                           for line in recipe["instructions"].split("\n") 
                           if line.strip())
    
    return f"""
    RECIPE: {recipe['title']}
    INGREDIENTS:
    {chr(10).join(f"- {ing}" for ing in ingredients)}
    
    INSTRUCTIONS:
    {instructions}
    """

def is_vegetarian(ingredients):
    """Check if recipe is vegetarian"""
    non_veg = {"chicken", "beef", "pork", "fish", "meat", "bacon", "lamb"}
    return not any(ing.lower() for ing in ingredients 
                  if any(meat in ing.lower() for meat in non_veg))