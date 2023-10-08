from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from langchain import LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from langchain.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain

template = """Human: {human_input}
ChatOSZ:"""

prompt = PromptTemplate(input_variables=["human_input"], template=template)

cllama_chain = LLMChain(
    llm="OSZ.bin",
    prompt=prompt,
    verbose=False,
    memory=ConversationBufferWindowMemory(k=2),
    llm_kwargs={"max_length": 4096}
)

def shkroter(input1):
    loader = WebBaseLoader("https://osdr.nasa.gov/bio/repo/search?q=&data_source=cgene,alsda&data_type=study")
    docs = loader.load()
    chain = load_summarize_chain(cllama_chain, chain_type="stuff")
    chain.run(docs)
    output = cllama_chain.predict(input1)
    return(output)

driver = webdriver.Chrome()
driver.get("https://osdr.nasa.gov/bio/repo/search?q=&data_source=cgene,alsda&data_type=study")
time.sleep(10)
for i in range(2, 12):
    link = driver.find_element(By.XPATH, "//div["+str(i)+"]//div[2]//p[1]//a[1]")
    im = driver.find_element(By.XPATH, "//div["+str(i)+"]//div[1]//a[1]//img[1]")
    tags = shkroter("Write only tags in one line for " + link.text)
    skhkr = shkroter("Write briefly the information only in one line from " + link.get_attribute("href"))
    print('    <div style="display: flex;">')
    print('        <img src="'+str(im.get_attribute("src"))+'" class="brain">')
    print('        <div style="margin-left: 10vmin; width: 50%;">')
    print('            <h1 href="'+str(link.get_attribute("href"))+'">'+str(link.text)+'</h1>')
    print('            <p style="font-size: 2.5vmin; font-style: italic;">'+str(tags)+'</p>')
    print('            <p>'+str(skhkr)+'</p>')
    print('        </div>')
    print('    </div>')
driver.close()