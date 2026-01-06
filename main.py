from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

# import os

load_dotenv()


def main():
    print("Hello from langchain-course!")
    # print(os.environ.get("OPENAI_API_KEY"))

    information = """
        Conor Anthony McGregor (born 14 July 1988) is an Irish professional mixed martial artist. He is a former Ultimate Fighting Championship (UFC) Featherweight and Lightweight Champion, becoming the first UFC fighter to hold UFC championships in two weight classes simultaneously.[11] He is also a former simultaneous Cage Warriors Fighting Championship (CWFC) Featherweight and Lightweight Champion.

        In 2008, McGregor began competing professionally in mixed martial arts (MMA), fighting in the lightweight and featherweight divisions. He won the CWFC Featherweight and Lightweight Championships in 2012 before signing with the UFC in 2013. After five consecutive wins, he won the Interim Featherweight Championship by defeating Chad Mendes at UFC 189. He became the undisputed Featherweight Champion at UFC 194 after knocking out José Aldo in 13 seconds, which is the fastest finish in UFC title fight history.[12] In 2017, he won the UFC Lightweight Championship at UFC 205 by defeating Eddie Alvarez.[13] He transitioned briefly to professional boxing, facing Floyd Mayweather Jr. in a highly publicised bout, which he lost via TKO in the 10th round.[14] He returned to MMA and challenged for the UFC Lightweight Championship at UFC 229, losing to Khabib Nurmagomedov via submission.[15]

        McGregor is the biggest pay-per-view (PPV) draw in MMA history, having headlined the five highest-selling UFC PPV events.[16] His fight against Nurmagomedov at UFC 229 drew 2.4 million PPV buys, the most ever for an MMA event.[17] His 2017 boxing match against Mayweather generated over 5.3 million buys across the United States and the United Kingdom, making it the second highest-selling pay-per-view event in history.[18][19][20] McGregor was ranked as the world's highest-paid athlete by Forbes in 2021, earning a reported $180 million.[21] He also appeared on the list in 2018, ranking fourth with earnings of $99 million.[22] Outside of fighting, McGregor has pursued business ventures.[23]

        McGregor has been involved in multiple legal issues, including civil and criminal cases. He has faced charges for assault, disorderly conduct, driving offences and rape. His comments on the 2023 Dublin riots and immigration policy in Ireland have also sparked controversy. In November 2024, an Irish High Court ruled in a civil case that he had assaulted and raped a woman in 2018, ordering him to pay over €248,000 in damages.[24] In December 2024, he was ordered to pay the victim's legal costs, amounting to approximately €1,500,000.[25] In July 2025, he lost an appeal on the verdict.[26] Following the 2024 civil court ruling, McGregor lost several sponsorship and partnership deals.[27][28]

        In March 2025, McGregor announced his intention to stand as an independent candidate in the 2025 Irish presidential election and has expressed views dubbed anti-immigration, far-right, and national populist.[29][30][31] On September 14, he withdrew from the election.[32]
    """

    summary_template = """
        Given the following information {information} about a person, I want you to create:
        1. A short summary of the person in 2-3 sentences.
        2. A list of 3 interesting facts about the person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    llm = ChatOpenAI(temperature=0, model="o3")

    # LangChain Expression Language (LCEL)
    chain = summary_prompt_template | llm
    response = chain.invoke(input={"information": information})
    print(response.content)


if __name__ == "__main__":
    main()
