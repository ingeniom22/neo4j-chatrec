from langchain_community.graphs import Neo4jGraph
from langchain.chains import GraphCypherQAChain
from langchain_community.chat_models.openai import ChatOpenAI
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

url = "neo4j+ssc://70abfeb2.databases.neo4j.io:7687"
username = "neo4j"
password = "MD7NxvfspehPHAjyqdn8_4dx30AM74ZPiukimdn76kc"

graph = Neo4jGraph(url=url, username=username, password=password, timeout=None)
graph.refresh_schema()
print(graph.schema)

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), graph=graph, verbose=True, return_direct=True
)

print(chain.run("Give me similar movies like Tank Girl (1995)"))
print(chain.run("Give me similar movies like Tank Girl (1995)"))