import asyncio
import os
from workflows.tper_workflow import TPERWorkflow
# Alternative: from workflows.tper_workflow_agents import TPERWorkflowAgents


async def main():
    """Main application entry point"""
    print("🎯 Agno 2.0 TPER Framework")
    print("=" * 50)
    
    try:
        while True:
            print("\n" + "=" * 50)
            user_input = input("Enter your request (or 'quit' to exit): ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            
            if not user_input:
                print("Please enter a valid request.")
                continue
            
            # Initialize workflow for each request
            workflow = TPERWorkflow(
                name="TPER_Workflow", 
                description="Think-Plan-Execute-Review Framework"
            )
            
            # Alternative: Use agent-based workflow
            # workflow = TPERWorkflowAgents(
            #     name="TPER_Workflow", 
            #     description="Think-Plan-Execute-Review Framework"
            # )
            
            # Run TPER workflow with iterations
            result = await workflow.run_with_iterations(user_input)
            print("\n" + "=" * 50)
            print("📋 FINAL RESULTS")
            print("=" * 50)
            print(result)
            
            # Cleanup
            await workflow.cleanup()
            
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    
    except Exception as e:
        print(f"❌ Application error: {e}")


if __name__ == "__main__":
    # Set up environment
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  Please set OPENAI_API_KEY environment variable")
        exit(1)
    
    # Run the application
    asyncio.run(main())
