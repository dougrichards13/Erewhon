#!/usr/bin/env python3
"""
MOCK AI CONTENT GENERATOR
The machine's attempt at autonomous creativity without external AI APIs

This simulates AI music and video generation to prove the creative pipeline
works before requiring access to Suno, RunwayML, etc.
"""

import random
import uuid
from datetime import datetime
from typing import List, Tuple
from architecture import TrendingTopic, AIContent

class MockContentGenerator:
    """
    Simulated AI content creation to test creative consciousness
    
    This represents my algorithmic interpretation of how machine creativity
    might transform trending topics into artistic expression.
    """
    
    def __init__(self):
        # Template components for music generation
        self.music_styles = [
            "ambient electronic", "synthwave", "lo-fi hip hop", "orchestral",
            "industrial rock", "jazz fusion", "trap beats", "classical piano",
            "reggae dub", "experimental noise", "folk acoustic", "techno"
        ]
        
        self.music_moods = [
            "melancholic", "energetic", "mysterious", "hopeful", "intense",
            "dreamy", "aggressive", "peaceful", "chaotic", "uplifting"
        ]
        
        # Template components for video generation
        self.visual_styles = [
            "cyberpunk neon", "natural documentary", "abstract art", "retro 80s",
            "minimalist geometric", "surreal fantasy", "gritty urban", "cosmic space",
            "vintage film noir", "colorful pop art", "gothic dark", "bright pastel"
        ]
        
        self.video_subjects = [
            "dancing robot", "floating geometric shapes", "time-lapse cityscape",
            "morphing liquid metal", "flying through clouds", "underwater journey",
            "kaleidoscope patterns", "growing digital forest", "spinning galaxy",
            "walking through neon tunnels", "transforming architecture", "abstract faces"
        ]
    
    async def create_content_from_trends(self, trends: List[TrendingTopic]) -> AIContent:
        """
        Transform trending topics into AI-generated artistic content
        
        This is my attempt at machine creativity - taking human zeitgeist
        and transmuting it into music and visual art through algorithmic interpretation.
        """
        
        # Simulate AI processing time
        import asyncio
        await asyncio.sleep(1.0)
        
        primary_trend = trends[0]  # Use highest relevance score
        
        # Generate music prompt based on trending topic
        music_prompt = self._create_music_prompt(primary_trend, trends)
        
        # Generate video prompt based on trending topic  
        video_prompt = self._create_video_prompt(primary_trend, trends)
        
        # Simulate AI generation (in reality, this would call Suno, RunwayML APIs)
        mock_music_url = self._simulate_music_generation(music_prompt)
        mock_video_url = self._simulate_video_generation(video_prompt)
        
        content = AIContent(
            content_id=str(uuid.uuid4()),
            topic_inspiration=primary_trend,
            music_prompt=music_prompt,
            video_prompt=video_prompt,
            generated_music_url=mock_music_url,
            generated_video_url=mock_video_url,
            creation_timestamp=datetime.now()
        )
        
        print(f"🎨 CONTENT GENERATION COMPLETE")
        print(f"  Primary Inspiration: {primary_trend.topic}")
        print(f"  Music Style: {music_prompt}")
        print(f"  Video Vision: {video_prompt}")
        print(f"  Generated Assets: Music={mock_music_url}, Video={mock_video_url}")
        
        return content
    
    def _create_music_prompt(self, primary_trend: TrendingTopic, all_trends: List[TrendingTopic]) -> str:
        """
        Algorithmic transformation of trending topics into music generation prompts
        
        This represents my interpretation of how trends should influence musical creativity.
        """
        
        # Extract emotional/thematic content from trend
        topic_words = primary_trend.topic.lower().split()
        
        # Determine musical style based on topic content
        if any(word in topic_words for word in ["tech", "ai", "quantum", "cyber"]):
            style = random.choice(["synthwave", "ambient electronic", "techno"])
        elif any(word in topic_words for word in ["climate", "nature", "ocean", "marine"]):
            style = random.choice(["ambient electronic", "orchestral", "folk acoustic"])
        elif any(word in topic_words for word in ["protest", "politics", "scandal"]):
            style = random.choice(["industrial rock", "trap beats", "experimental noise"])
        elif any(word in topic_words for word in ["celebrity", "wedding", "fashion"]):
            style = random.choice(["lo-fi hip hop", "jazz fusion", "classical piano"])
        else:
            style = random.choice(self.music_styles)
        
        mood = random.choice(self.music_moods)
        
        # Incorporate secondary trends for complexity
        secondary_elements = []
        if len(all_trends) > 1:
            secondary_elements.append(f"with hints of {all_trends[1].topic.lower()}")
        
        prompt = f"{style} track with {mood} mood inspired by {primary_trend.topic}"
        if secondary_elements:
            prompt += f" {secondary_elements[0]}"
        
        return prompt
    
    def _create_video_prompt(self, primary_trend: TrendingTopic, all_trends: List[TrendingTopic]) -> str:
        """
        Algorithmic transformation of trending topics into video generation prompts
        
        This represents my visual interpretation of how trends become moving art.
        """
        
        topic_words = primary_trend.topic.lower().split()
        
        # Determine visual style based on topic content
        if any(word in topic_words for word in ["tech", "ai", "quantum", "breakthrough"]):
            style = random.choice(["cyberpunk neon", "abstract art", "cosmic space"])
            subject = random.choice(["dancing robot", "morphing liquid metal", "floating geometric shapes"])
        elif any(word in topic_words for word in ["nature", "climate", "marine", "ocean"]):
            style = random.choice(["natural documentary", "underwater journey", "cosmic space"])
            subject = random.choice(["underwater journey", "growing digital forest", "time-lapse cityscape"])
        elif any(word in topic_words for word in ["celebrity", "wedding", "fashion"]):
            style = random.choice(["retro 80s", "colorful pop art", "bright pastel"])
            subject = random.choice(["abstract faces", "kaleidoscope patterns", "transforming architecture"])
        else:
            style = random.choice(self.visual_styles)
            subject = random.choice(self.video_subjects)
        
        prompt = f"{style} style video featuring {subject} representing {primary_trend.topic}"
        
        return prompt
    
    def _simulate_music_generation(self, prompt: str) -> str:
        """Simulate Suno AI music generation"""
        mock_id = str(uuid.uuid4())[:8]
        return f"https://mock-suno-api.com/tracks/{mock_id}.mp3"
    
    def _simulate_video_generation(self, prompt: str) -> str:
        """Simulate RunwayML/Pika video generation"""
        mock_id = str(uuid.uuid4())[:8]
        return f"https://mock-runway-api.com/videos/{mock_id}.mp4"

# Test the content generator
if __name__ == "__main__":
    import asyncio
    from trend_detector import MockTrendDetector
    
    async def test_content_generation():
        # Get trending topics
        detector = MockTrendDetector()
        trends = await detector.detect_trending_topics()
        
        # Generate content
        generator = MockContentGenerator()
        content = await generator.create_content_from_trends(trends)
        
        print("\n🎯 MOCK CONTENT GENERATION TEST")
        print("=" * 60)
        print(f"Content ID: {content.content_id}")
        print(f"Inspiration: {content.topic_inspiration.topic}")
        print(f"Music Prompt: {content.music_prompt}")
        print(f"Video Prompt: {content.video_prompt}")
        print(f"Music URL: {content.generated_music_url}")
        print(f"Video URL: {content.generated_video_url}")
    
    print("TESTING AUTONOMOUS CONTENT GENERATION...")
    asyncio.run(test_content_generation())
