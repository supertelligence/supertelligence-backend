import asyncio
import uvicorn
import multiprocessing
import sys
import os
from pathlib import Path

# Add the src directory to the path so we can import our modules
sys.path.insert(0, str(Path(__file__).parent))

from discord_bot import main as run_discord_bot

def run_fastapi():
    """Run the FastAPI server"""
    print("Starting FastAPI server...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

def run_bot():
    """Run the Discord bot"""
    print("Starting Discord bot...")
    asyncio.run(run_discord_bot())

async def main():
    """Main function to run both services"""
    print("🚀 Starting Supertelligence Services...")
    print("=" * 50)
    
    # Check for required environment variables
    required_vars = ["DISCORD_BOT_TOKEN", "OPENAI_API_KEY"]
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n📝 Please create a .env file with the required variables.")
        print("   See env.example for reference.")
        return
    
    # Create processes for FastAPI and Discord bot
    api_process = multiprocessing.Process(target=run_fastapi)
    bot_process = multiprocessing.Process(target=run_bot)
    
    try:
        # Start both processes
        api_process.start()
        bot_process.start()
        
        print("✅ Both services started successfully!")
        print("📡 FastAPI server: http://localhost:8000")
        print("🤖 Discord bot: Connected and ready!")
        print("\nPress Ctrl+C to stop all services...")
        
        # Wait for both processes
        api_process.join()
        bot_process.join()
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down services...")
        api_process.terminate()
        bot_process.terminate()
        api_process.join()
        bot_process.join()
        print("✅ All services stopped.")

if __name__ == "__main__":
    multiprocessing.set_start_method('spawn', force=True)
    asyncio.run(main()) 