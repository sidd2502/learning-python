import urllib

def read_text():
    quotes = open(r"C:\Users\zotech_pc\Desktop\Check Profan.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profan(content)

def check_profan(check):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+check)
    output = conn.read()
    print(output)
    conn.close()

read_text()
