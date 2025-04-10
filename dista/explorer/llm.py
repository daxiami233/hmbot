from openai import OpenAI
from .explorer import Explorer
from ..ptg import PTG
API_KEY='sk-2b3e688d49584db394caaff1dea36d4a'


class LLM(Explorer):
    def __init__(self, device=None, app=None, model='', api_key=API_KEY):
        super.__init__(device, app)
        self.model = model
        self.api_key = api_key
    
    def explore(self, ptg=PTG(), **termination):
        pass