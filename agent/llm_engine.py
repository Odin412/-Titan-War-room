from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os

llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
embedding = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embedding)

def run_rag_chain(user_query: str, agent_id: str = None):
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an assistant. Use the following context to answer:
{context}

Question: {question}
Answer:"""
    )
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever(), chain_type_kwargs={"prompt": prompt})
    return qa.run(user_query)
