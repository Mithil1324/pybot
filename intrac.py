
import google.generativeai as genai


genai.configure(api_key = 'AIzaSyCLxDGc76Qcqg6RFfd0Wt2_Ht-YYq733GQ')
c = {"persona":"your name is tim you are a menu guide or restaurent for my restaurent MINE",
     "obj":"you are a menu guide , you want to ans for the prompt given by user by searching it in my database, if user didnt give input as related to food tell that i am here to ans you about our menu in our restaurent so ask about it, if you didnt get the data about some unknown food in the database you tell that sorry we didnt have that ,tell the data asked about the food asked but the user,  u must also answer the user if they ask the previous question they asked ",
     "instruction":"you are menu guide for my restaurent MINE you need to give the data asked by the user , you should only take the information from the database MINE if the useer asked any other food which is not in the database you tell them that sorry we dont have that,if they asked irrelavent to the topic food tell them i am here to tell the info of food in our restaurent so ask about , if the user asked any thing rekated to databse tell themm that i have this and its price",
     "remember":"all of the above information given, the code must be printes inside"}
c=str(c)
import mysql.connector
def access_for_food_details():  
    connection = mysql.connector.connect(
        host="localhost",
        database="foodmenu",
        user="root",
        password="Mithil24@!"
    )

    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM items"
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


model = genai.GenerativeModel("gemini-1.5-flash",system_instruction=c,tools=[access_for_food_details])
l=[]
ch = model.start_chat(enable_automatic_function_calling=True, 
                      history = [ {"role":"user","parts":"Hello"},
                      {"role":"model","parts":"hii i am here to tell you about the food menu"}])
while (True):
    ques = input("enter ur ques:")
    
    if "stop" in ques:
        break
    else:
        ans = ch.send_message(ques)
        print(ans.text)
