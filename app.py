"""
@author: Priyang Bhatt
"""
import streamlit as st
import joblib
import numpy as np

# Set the page config
st.set_page_config(page_title='Health Insurance Cost Prediction', page_icon='🏥', layout='wide')

# Function to add a background image
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://imgv3.fotor.com/images/share/Free-blue-gradient-pattern-background-from-Fotor.jpg");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_url()

def main():
    # Display an image at the top

    # Custom HTML for header
    html_temp = """
    <img src="https://img.freepik.com/premium-vector/abstract-health-medical-science-healthcare-icon-digital-technology-doctor-concept-modern_36402-1323.jpg" style ="display: block;margin-left: auto;margin-right: auto;width: 50%;padding-bottom:45px"/>
    <div style="background-color:rgba(1,8,34,255);padding:16px;border-radius:10px;">
    <h2 style="color:rgba(112, 211, 252, 0.84);text-align:center;font-family:'Courier New';">Health Insurance Premium Predictor</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_rf')
    
    # Input fields
    p1 = st.slider('Enter Your Age', 18, 100, 25, key='age_slider', help="Slide to select your age")
    
    s1 = st.selectbox('Sex', ('Male', 'Female'), help="Select your gender")
    p2 = 1 if s1 == 'Male' else 0
    
    p3 = st.number_input("Enter Your BMI Value", min_value=0.0, max_value=50.0, step=0.1, help="Enter your Body Mass Index value")
    
    p4 = st.slider("Enter Number of Children", 0, 4, 0, help="Slide to select the number of children you have")
    
    s2 = st.selectbox("Smoker", ("Yes", "No"), help="Select if you are a smoker")
    p5 = 1 if s2 == 'Yes' else 0
    
    s3 = st.selectbox("Region", ("Southwest", "Southeast", "Northwest", "Northeast"), help="Select your region")
    region_dict = {"Southwest": 1, "Southeast": 2, "Northwest": 3, "Northeast": 4}
    p6 = region_dict[s3]

    # Predict button
    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.balloons()
        st.success('Your Insurance Cost is Rs {} / yr'.format(round(pred[0], 2)))
        
        
    
    st.markdown(
        """
        **Health insurance policy** is an assurance which provides immediate financial help in case when any medical emergency arises. 
        It is a contract between a policyholder and the insurance company which covers medical expenses that might occur due to illness, 
        injury or accident. If you have a health insurance policy, then some or all the medical expenses will be borne by the insurance company, 
        against which an insured is supposed to pay a certain amount known as premium.
        """
    )
    
    st.markdown(
        """
        ### Why Should I Have A Health Insurance Policy?

        Purchasing a health insurance plan is something that we all avoid till the time we understand its importance. 
        Before buying one, it is crucial to understand the various benefits of a health insurance plan as medical emergencies 
        can knock anytime and could make a big hole in your pocket. Therefore, it is advisable to buy a health insurance 
        policy at a very young age, where one can have the comprehensive coverage at an affordable premium cost, plus you 
        also get the advantage of tax deductions on premium paid.

        In a nutshell, one should purchase a health insurance policy because:

        - It facilitates you to get superior medical treatment without any worry of high medical costs.
        - Offers specialized coverage for critical illnesses.
        - Covers road emergency ambulance costs.
        - Offers an affordable premium for youngsters.
        - Provides cashless claim benefit, which allows you to take care of your health instead of worrying about hefty medical bills.
        - Protect your savings during medical emergencies.
        - Provides tax benefits under Section 80D.
        - Lastly, it safeguards you and your family and protects your savings.
        """
    )
    
    st.markdown(
        """
        ### Types Of Health Insurance Policies

        There are basically two kinds of health insurance policies such as individual or self-plan and family floater policy. 
        As the name suggests, an individual policy would only provide coverage and benefits to the main policyholder. 
        On the other hand, in the case of a family floater plan, there is only one plan which provides coverage to your 
        entire family such as spouse, dependent children, parent and parent-in-laws or dependent siblings.

        One should select the plan, depending upon the factors such as your age, family medical history, children’s age, 
        medical history and of course one’s budget.  Let’s understand about each of these plans in detail:
        """
    )
    
    st.markdown(
        """
        #### Individual or Self Health Insurance Plan

        An individual health insurance policy is issued under the name of a single policyholder, which means that the sum insured 
        coverage and the benefits of the policy are totally dedicated to the insured and cover no one else. Here, the individual 
        purchases the policy to maintain their own health which in turn provides financial help in case of their own medical emergency.
        """
    )

    st.markdown(
        """
        #### Family Floater Health Insurance Plan

        Family floater health insurance is one policy which aims to provide sum insured coverage to individual and as well his family 
        members. Rather than taking a single policy for each member of the family, the family health insurance plan is a better 
        option, as it acts as an umbrella for the entire family. Here the sum assured coverage is shared by all the members who have 
        been covered under the same plan.

        However, it is advisable to have a separate plan for your senior citizen parent or parent-in-laws as it will prove to be a more 
        affordable option. Similarly, if any member in the family has a huge medical history, then it is also better to buy a separate 
        plan for them rather than covering them in the family floater plan.
        """
    )

    st.markdown(
        """
        ### Factors To Consider Before Deciding On A Health Insurance Plan

        **Step 1: Finding the Right Insurance Company**

        Here are some factors that you can use in deciding on the right health insurance company:

        1. **The Range of Plans Offered**: Check out the different types of plans that a company offers as well as the plan USPs.
        Some companies offer a range of products to suit the varied coverage requirements that you have. Choose a company with a 
        diverse range of plans so that you can find the right policy suiting your needs.
        2. **The Network of Hospitals**: The network of hospitals is extremely important for availing cashless claims. The wider the network that an insurer has, the better it would be. This would allow you to locate the nearest cashless hospital with ease.

       3. **Claim Settlement Ratio**: The claim settlement ratio points to one thing – what percentage of claims did the company settle in a financial year. A higher ratio indicates that the company is steadfast in settling its claims. A factor that works in favor of the insurer.

       4. **Claim-Based Loading**: Some companies tend to increase the renewal premium if you made claims in the previous years. This converts to higher premium expenses. As such, avoid companies that follow this practice.

       5. **Premium Rate**: Pricing policy is how much premium the company charges vis-à-vis its competitors. You can check the pricing policy by comparing similar plans across different companies. For instance, the Aarogya Sanjeevani policy offers uniform coverage features across all insurers. Its premiums, however, depend on the insurer’s pricing policy. Compare the premium of the plan across insurers to find the insurer that charges the least. Chances are, its pricing policy would be fair across all its plans.

       6. **Ease of Claim Settlement**: Insurers have revolutionized their claim process and made it simpler. The following concepts are gaining traction:
       - AI-enabled claim processing
       - WhatsApp intimation
       - Digital documentation
       - Quicker approvals
       - App-based claim intimation and tracking, etc.
       Such facilities speed up the claim process and make it hassle-free. Thus, look for insurers that provide such facilities for quicker claim settlements.

       7. **Reviews**: Lastly, don’t ignore customer testimonials and reviews. Most insurers showcase their customers’ reviews on their websites. You can check them out. Alternatively, you can talk to your friends and relatives about their insurers. If they have made a claim, find out their claim experience to know which company follows the best practices.
        """
    )

# Run the app
if __name__ == '__main__':
    main()
