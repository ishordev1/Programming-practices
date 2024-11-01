import axios from "axios";
import react, { useEffect, useState } from "react"
export default function Dashboard() {
    const [user, setUser] = useState(null);
    useEffect(() => {
        axios.get("http://localhost:8080/user-info", { withCredentials: true })
            .then(response => {
                setUser(response.data)
            }).catch(error=>{
                console.log("error occor"+error)
            })
    }, []);

    return (
        <>
     
            <h1>this is dashboard page</h1>
            {user ? (
                <div className="">
                    <p><strong>Name:</strong>{user.name}</p>
                    <p><strong>Email:</strong>{user.email}</p>
                    {user.picture && (<img src={user.picture} alt="user-picture"/>)}
                </div>
            ) :
                (
                    <h1>loading</h1>
                )

            }

        </>
    );
}