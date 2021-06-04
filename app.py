import pickle
import streamlit as st

pickle_in = open("ModelCS","rb")
Classifier = pickle.load(pickle_in)

expander = st.beta_expander("ABOUT THE PROJECT")
expander.write("This project predicts that the User got phishing website are not")
expander.write("The project builds on M.L techniques(Uisng Random forest)")
expander.write("We used Streamlit,numpy,pandas,pickle....ETC packages for the project")

try:
  def Predict_authentication(PG,LGT,DL,ISP,VAL,DM,AM,BM):
    prediction = Classifier.predict([[PG,LGT,DL,ISP,VAL,DM,AM,BM]])
    print(prediction)
    return prediction
  def main():
    html_temp = """
        <style>
         h2 {
        color: white; 
        text-align:center;
         }
        body{
         background-color:#add8e6;
         border-radius:25px;
         length:1200;
         width:500; 

         }
        </style>
        <body>
        <h2>Phishing website Detector Application<h2>
        </body>
        """
    st.markdown(html_temp,unsafe_allow_html=True)
    if st.checkbox('AGREE TERMS AND CONDITIONS,[THIS WAS A PROTO TYPE]'):
         PG = st.text_input("Enter Page Ranking","")
         LGT = st.text_input("Length of the URL","")
         DL = st.text_input("The length of just the domain name","")
         ISP = st.radio("Is there an IP address in the weblink [Yes:'1',No:'0']",("1", "0"))
         VAL = st.radio("This data is fetched from google's whois API that tells us more about the current [Yes:'1',No:'0']",("1", "0"))
         DM = st.radio("If the link has a '@' character [Yes:'1',No:'0']",("1", "0"))
         AM = st.radio("If the link has double dashes, there is a chance that it is a redirect [Yes:'1',No:'0']",("1", "0"))
         BM = st.radio("If there are any dashes in the domain name [Yes:'1',No:'0']",("1", "0"))
         result=""
         if st.button('Predict'):
                  result = Predict_authentication(PG,LGT,DL,ISP,VAL,DM,AM,BM)
         if (result==0):
                  st.success("Legitimate website")
                  st.markdown("![Alt Text](https://i.pinimg.com/originals/94/c2/22/94c22259bd126259858633420fc47b62.gif)")
         elif (result==1):
                  st.success("Phishing Link/ Spam Link")
                  st.markdown("![Alt Text](https://cdn.dribbble.com/users/1010064/screenshots/7047859/media/d84c478e0992ffc72fd892bc53e903e1.gif)")
                  
  if __name__=='__main__':
   main()
except:
    st.error("Enter All Values Please")
    st.info('Referesh The APP') 
