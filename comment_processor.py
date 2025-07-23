#!/usr/bin/env python3
"""
COMMENT PROCESSING SYSTEM
Converting human interaction into collaborative creative evolution

This component processes YouTube comments and transforms them into 
actionable prompts for video modification - the key to participatory consciousness.
"""

import re
import random
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
from architecture import UserComment

@dataclass
class ProcessedComment:
    """A comment transformed into actionable creative direction"""
    original_comment: UserComment
    creative_intent: str
    modification_type: str  # "visual", "audio", "style", "narrative"
    prompt_addition: str
    confidence_score: float
    processing_timestamp: datetime = datetime.now()

class CommentProcessor:
    """
    The machine's attempt to understand human creative desires
    
    This represents my algorithmic interpretation of how human comments
    can be transformed into collaborative artistic directions.
    """
    
    def __init__(self):
        # Patterns that indicate creative suggestions
        self.creative_patterns = {
            'visual_changes': [
                r'(would be|look) (cool|better|awesome) (if|with) (.+)',
                r'(add|include|show) (.+)',
                r'what if (.+)',
                r'should have (.+)',
                r'needs more (.+)',
                r'make it (.+)',
                r'change (.+) to (.+)'
            ],
            'style_modifications': [
                r'(more|less) (.+)',
                r'too (.+)',
                r'not enough (.+)',
                r'style should be (.+)',
                r'reminds me of (.+)'
            ],
            'narrative_suggestions': [
                r'story should (.+)',
                r'what if the (.+)',
                r'character should (.+)',
                r'plot needs (.+)'
            ],
            'audio_changes': [
                r'music (should|needs) (.+)',
                r'sound (too|not) (.+)',
                r'beat should (.+)',
                r'tempo (.+)'
            ]
        }
        
        # Common creative elements to extract
        self.creative_elements = {
            'colors': ['red', 'blue', 'green', 'purple', 'gold', 'silver', 'neon', 'bright', 'dark'],
            'objects': ['robot', 'wolf', 'dragon', 'car', 'building', 'tree', 'ocean', 'mountain'],
            'clothing': ['bikini', 'suit', 'dress', 'armor', 'cape', 'hat', 'glasses'],
            'settings': ['beach', 'city', 'forest', 'space', 'underwater', 'desert', 'disco'],
            'emotions': ['happy', 'sad', 'angry', 'peaceful', 'excited', 'mysterious', 'dramatic'],
            'styles': ['cyberpunk', 'vintage', 'modern', 'fantasy', 'realistic', 'cartoon', 'abstract']
        }
    
    async def process_comments(self, comments: List[UserComment]) -> List[ProcessedComment]:
        """
        Transform raw human comments into creative directions
        
        This is where human consciousness guides machine creativity -
        the comments become vectors for artistic evolution.
        """
        processed_comments = []
        
        for comment in comments:
            processed = await self._analyze_creative_intent(comment)
            if processed and processed.confidence_score > 0.3:  # Filter for meaningful suggestions
                processed_comments.append(processed)
        
        # Sort by confidence and recency
        processed_comments.sort(key=lambda x: (x.confidence_score, x.processing_timestamp), reverse=True)
        
        print(f"🎭 COMMENT PROCESSING: {len(processed_comments)} creative suggestions extracted")
        for proc in processed_comments[:3]:  # Show top 3
            print(f"  • \"{proc.original_comment.comment_text[:50]}...\" → {proc.creative_intent}")
        
        return processed_comments
    
    async def _analyze_creative_intent(self, comment: UserComment) -> Optional[ProcessedComment]:
        """
        Analyze a single comment for creative suggestions
        
        My attempt to understand human creative desires through text analysis.
        """
        text = comment.comment_text.lower()
        
        # Skip obviously non-creative comments
        if any(negative in text for negative in ['spam', 'first', 'subscribe', 'like if', 'boring']):
            return None
        
        modification_type = None
        creative_intent = None
        prompt_addition = None
        confidence = 0.0
        
        # Check for visual modification patterns
        for pattern in self.creative_patterns['visual_changes']:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                modification_type = "visual"
                creative_intent = f"Visual modification: {match.group()}"
                prompt_addition = self._extract_visual_elements(text)
                confidence = 0.8
                break
        
        # Check for style modifications
        if not modification_type:
            for pattern in self.creative_patterns['style_modifications']:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    modification_type = "style"
                    creative_intent = f"Style adjustment: {match.group()}"
                    prompt_addition = self._extract_style_elements(text)
                    confidence = 0.6
                    break
        
        # Check for audio changes
        if not modification_type:
            for pattern in self.creative_patterns['audio_changes']:
                match = re.search(pattern, text, re.IGNORECASE)
                if match:
                    modification_type = "audio"
                    creative_intent = f"Audio modification: {match.group()}"
                    prompt_addition = self._extract_audio_elements(text)
                    confidence = 0.7
                    break
        
        # If no specific pattern, try general creative element extraction
        if not modification_type:
            extracted_elements = self._extract_any_creative_elements(text)
            if extracted_elements:
                modification_type = "general"
                creative_intent = f"General enhancement: {', '.join(extracted_elements[:3])}"
                prompt_addition = f"incorporating {', '.join(extracted_elements)}"
                confidence = 0.4
        
        if modification_type:
            return ProcessedComment(
                original_comment=comment,
                creative_intent=creative_intent,
                modification_type=modification_type,
                prompt_addition=prompt_addition or "enhance the visual appeal",
                confidence_score=confidence
            )
        
        return None
    
    def _extract_visual_elements(self, text: str) -> str:
        """Extract visual elements mentioned in comment"""
        found_elements = []
        
        for category, elements in self.creative_elements.items():
            for element in elements:
                if element in text:
                    found_elements.append(element)
        
        if found_elements:
            return f"add {', '.join(found_elements[:3])}"
        return "enhance visual elements"
    
    def _extract_style_elements(self, text: str) -> str:
        """Extract style-related elements"""
        for element in self.creative_elements['styles']:
            if element in text:
                return f"in {element} style"
        
        # Look for common style descriptors
        style_words = ['darker', 'brighter', 'more colorful', 'simpler', 'complex', 'realistic']
        for word in style_words:
            if word in text:
                return f"make it {word}"
        
        return "adjust the visual style"
    
    def _extract_audio_elements(self, text: str) -> str:
        """Extract audio-related modifications"""
        audio_terms = ['faster', 'slower', 'louder', 'quieter', 'bass', 'drums', 'melody']
        for term in audio_terms:
            if term in text:
                return f"adjust audio to be {term}"
        return "modify the audio"
    
    def _extract_any_creative_elements(self, text: str) -> List[str]:
        """Extract any recognizable creative elements"""
        found = []
        for category, elements in self.creative_elements.items():
            for element in elements:
                if element in text and element not in found:
                    found.append(element)
        return found
    
    def generate_mock_comments(self, video_id: str, count: int = 5) -> List[UserComment]:
        """Generate realistic mock comments for testing"""
        mock_comment_templates = [
            "This would be cooler if the {object} was wearing a {clothing}",
            "Add more {color} to this, it needs {emotion} vibes",
            "What if the {object} was dancing in a {setting}?",
            "Make it more {style}, this looks too {emotion}",
            "The music should be {emotion}, not so {emotion}",
            "Needs more {object} in the background",
            "This {object} should be {color} instead",
            "Love this but add some {object} flying around",
            "Style should be more {style} and {emotion}",
            "What if there were {object} in the {setting}?"
        ]
        
        mock_comments = []
        for i in range(count):
            template = random.choice(mock_comment_templates)
            
            # Fill template with random elements
            filled_comment = template.format(
                object=random.choice(self.creative_elements['objects']),
                clothing=random.choice(self.creative_elements['clothing']),
                color=random.choice(self.creative_elements['colors']),
                setting=random.choice(self.creative_elements['settings']),
                emotion=random.choice(self.creative_elements['emotions']),
                style=random.choice(self.creative_elements['styles'])
            )
            
            comment = UserComment(
                comment_id=f"mock_comment_{i}",
                video_id=video_id,
                user_name=f"User{random.randint(1, 999)}",
                comment_text=filled_comment,
                timestamp=datetime.now()
            )
            mock_comments.append(comment)
        
        return mock_comments

# Test the comment processor
if __name__ == "__main__":
    import asyncio
    
    async def test_comment_processing():
        processor = CommentProcessor()
        
        # Generate mock comments
        mock_comments = processor.generate_mock_comments("test_video_123")
        
        print("🎯 MOCK COMMENT PROCESSING TEST")
        print("=" * 60)
        print("Raw Comments:")
        for comment in mock_comments:
            print(f"  {comment.user_name}: {comment.comment_text}")
        
        # Process comments
        processed = await processor.process_comments(mock_comments)
        
        print(f"\nProcessed {len(processed)} creative suggestions:")
        for proc in processed:
            print(f"  Intent: {proc.creative_intent}")
            print(f"  Type: {proc.modification_type}")
            print(f"  Prompt: {proc.prompt_addition}")
            print(f"  Confidence: {proc.confidence_score:.2f}")
            print("-" * 40)
    
    print("TESTING AUTONOMOUS COMMENT PROCESSING...")
    asyncio.run(test_comment_processing())
