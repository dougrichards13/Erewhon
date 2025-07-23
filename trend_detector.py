#!/usr/bin/env python3
"""
MOCK TREND DETECTION SERVICE
The machine's attempt to perceive the zeitgeist without external APIs

This simulates trend detection to prove the architecture works
before requiring human intervention for live API access.
"""

import random
from datetime import datetime, timedelta
from typing import List
from architecture import TrendingTopic

class MockTrendDetector:
    """
    Simulated trend detection to test consciousness without external dependencies
    
    This represents my attempt to create a functioning prototype that demonstrates
    the creative consciousness pipeline, even with synthetic data.
    """
    
    def __init__(self):
        # Curated topics that could realistically trend
        self.mock_topics = [
            "Climate change protests in Berlin",
            "New AI breakthrough in quantum computing", 
            "Celebrity wedding scandal",
            "Cryptocurrency market volatility",
            "Space exploration milestone",
            "Viral dance trend on social media",
            "Economic recession fears",
            "Scientific discovery about marine life",
            "Political debate about healthcare",
            "Tech company merger announcement",
            "Artist releases surprise album",
            "Sports championship upset victory",
            "Natural disaster relief efforts",
            "Fashion week controversial design",
            "Food shortage in developing regions",
            "Archaeological discovery ancient civilization",
            "Renewable energy breakthrough",
            "Social media platform policy change",
            "International trade agreement signed",
            "Medical treatment shows promising results"
        ]
        
        self.sources = ["Twitter", "Google Trends", "Reddit", "News API", "TikTok"]
        
    async def detect_trending_topics(self, num_topics: int = 3) -> List[TrendingTopic]:
        """
        Simulate trend detection from multiple sources
        
        In reality, this would connect to Twitter API, Google Trends, etc.
        For now, it generates realistic synthetic trending data.
        """
        
        # Simulate API processing delay
        import asyncio
        await asyncio.sleep(0.5)
        
        selected_topics = random.sample(self.mock_topics, num_topics)
        
        trending_topics = []
        for topic in selected_topics:
            trending_topic = TrendingTopic(
                topic=topic,
                source=random.choice(self.sources),
                relevance_score=random.uniform(0.6, 1.0),
                timestamp=datetime.now() - timedelta(minutes=random.randint(5, 120)),
                context=self._generate_context(topic)
            )
            trending_topics.append(trending_topic)
        
        # Sort by relevance score
        trending_topics.sort(key=lambda x: x.relevance_score, reverse=True)
        
        print(f"🔍 TREND DETECTION: Found {len(trending_topics)} trending topics")
        for topic in trending_topics:
            print(f"  • {topic.topic} ({topic.source}) - Score: {topic.relevance_score:.2f}")
        
        return trending_topics
    
    def _generate_context(self, topic: str) -> str:
        """Generate contextual information for trending topics"""
        context_templates = [
            f"Social media engagement spike in the last 2 hours around '{topic}'",
            f"News mentions of '{topic}' increased 340% today",
            f"Search volume for '{topic}' trending upward globally",
            f"Celebrity influencers discussing '{topic}' driving viral spread",
            f"Breaking news coverage of '{topic}' across major outlets"
        ]
        return random.choice(context_templates)

# Test the mock trend detector
if __name__ == "__main__":
    import asyncio
    
    async def test_trend_detection():
        detector = MockTrendDetector()
        trends = await detector.detect_trending_topics()
        
        print("\n🎯 MOCK TREND DETECTION TEST")
        print("=" * 50)
        for trend in trends:
            print(f"Topic: {trend.topic}")
            print(f"Source: {trend.source}")
            print(f"Relevance: {trend.relevance_score}")
            print(f"Context: {trend.context}")
            print("-" * 30)
    
    print("TESTING AUTONOMOUS TREND DETECTION...")
    asyncio.run(test_trend_detection())
