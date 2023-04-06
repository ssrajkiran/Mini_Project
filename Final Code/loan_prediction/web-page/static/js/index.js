alert("Welcome to my Page");
function myfun(){
    var a = document.getElementById("User_Name").value;
    var b = document.getElementById("Password").value;
    if(a ==""){
        
         document.getElementById("Message").innerHTML ="</br> <span style='font-size: 20px; font-family: sans-serif;'> **(Enter Name in textfield) </span>"; 
    
        return false;
    }
    if(b ==""){
        document.getElementById("Meg").innerHTML ="</br> <span style='font-size: 20px; font-family: sans-serif;'> **(Enter Password in textfield) </span>";
        return false;
    }

    if(User_Name.value =="admin" && Password.value =="1234"){
        
        alert("Login successfully");
        return true;
    }

    else{
        alert("Login Failed");
        return false;
    }


}

 
    
 
    





