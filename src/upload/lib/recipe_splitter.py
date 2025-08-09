from typing import List, Dict, Union
import json
from langchain_core.documents import Document

class RecipeSplitter:
    def __init__(self):
        # No need for text splitter since we're storing whole recipes
        pass
    
    def process_recipe(self, recipe_id: str, recipe_data: Dict) -> List[Document]:
        """Process a single recipe into one complete document with metadata"""
        # Clean ingredients list
        ingredients = [
            ing.replace("ADVERTISEMENT", "").strip() 
            for ing in recipe_data["ingredients"] 
            if ing.strip() and not ing.isspace()
        ]
        
        # Clean instructions
        instructions = "\n".join(
            line.strip() 
            for line in recipe_data["instructions"].split("\n") 
            if line.strip()
        )
        
        # Create one comprehensive document per recipe
        doc = Document(
            page_content=f"""
            RECIPE: {recipe_data['title']}
            INGREDIENTS:
            {chr(10).join(f"- {ing}" for ing in ingredients)}
            
            INSTRUCTIONS:
            {instructions}
            
            COOK TIME: {recipe_data.get('cook_time', 'Not specified')}
            """,
            metadata={
                "recipe_id": recipe_id,
                "title": recipe_data["title"],
                "vegetarian": self.is_vegetarian(ingredients),
                "main_ingredients": self.get_main_ingredients(ingredients),
                "picture_link": recipe_data.get("picture_link", ""),
                "source": "imported_recipes"
            }
        )
        
        return [doc]

    def is_vegetarian(self, ingredients: List[str]) -> bool:
        """Check if recipe is vegetarian"""
        non_veg_keywords = ["chicken", "beef", "pork", "lamb", "fish", "meat", "bacon"]
        return not any(
            keyword in ingredient.lower()
            for ingredient in ingredients
            for keyword in non_veg_keywords
        )

    def get_main_ingredients(self, ingredients: List[str]) -> List[str]:
        """Extract 3-5 main ingredients"""
        # Filter out common non-main ingredients
        common_words = {"salt", "pepper", "oil", "water", "sugar", "flour"}
        main_ingredients = [
            ing.split(",")[0].split("(")[0].strip()  # Take first part before any commas/parens
            for ing in ingredients
            if not any(word in ing.lower() for word in common_words)
        ]
        return main_ingredients[:5]  # Return top 5

    def process_json_file(self, file_path: str) -> List[Document]:
        """Process a JSON file with multiple recipes"""
        with open(file_path) as f:
            recipes_data = json.load(f)

        print(f"Loaded {len(recipes_data)} recipes")
        
        all_docs = []
        for recipe_id, recipe in recipes_data.items():
            all_docs.extend(self.process_recipe(recipe_id, recipe))
            
        return all_docs