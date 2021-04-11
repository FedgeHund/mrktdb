import axios from 'axios';
import { URL } from '../App.js';


export const checkUser = async () => {
    await axios.get("http://" + URL + "/auth/user/", {
    },
        {
            headers: {
                "Content-Type": 'application/json'
            }
        }
    )
        .then(function (response) {
            if (response.status == 200) {
                console.log(response.data);
            }
            else {
                //window.location = "http://127.0.0.1:8000/signin/"
                console.log(response);
            }
        })
};