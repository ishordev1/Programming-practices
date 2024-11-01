import react from "react"

const Home=()=>{
const githubLogin=()=>{
window.location.href="http://localhost:8080/oauth2/authorization/github"
}

const googleLogin=()=>{
window.location.href="http://localhost:8080/oauth2/authorization/google"
}
    return (
        <>
        <h1>Welcom To Login Page</h1>
        <button onClick={githubLogin} >Login with Github</button>
        <button  onClick={googleLogin}>Login with Google</button>
        </>
    );
}
export default Home;