from src.langgraph.state.state import State

class BasicChatbotNode:
    """
    Basic Chatbot logic Implementation.
    """
    
    def __init__(self, model):
        self.llm= model
        
    def process(self, state: State):
        """
        Process the input state and generates a chatbot response. 
        """
        
        return {"messages":self.llm.invoke(state['messages'])}
    