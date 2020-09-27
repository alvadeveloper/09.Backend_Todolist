const loginweb = "https://dev-rp5hh-6z.auth0.com/authorize?audience=todo&response_type=token&client_id=2MdOSeT1x6aGKdtQPfPGbC9i6r99Ihoq&redirect_uri=http://localhost:8080"

export const login=()=>{
  document.getElementById('login').addEventListener('click', ()=>{
    window.location.href=loginweb
  })
}

export const geturl=()=>{
  const a = window.location.hash
  if (a.length > 0){
    const b = a.split("=")[1]
    const c = b.split("&expires")[0]
    console.log(c)
    document.getElementById('token').textContent = c
  }
}

