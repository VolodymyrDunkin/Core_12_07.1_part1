TRANS = {ord("a"): "AAA",
         ord("b"):"BBB"}


def normalize(text:str):
    return text.translate(TRANS)
    
    
if __name__ == "__main__":

    print(normalize("abrtyab"))