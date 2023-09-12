const loginForm = document.getElementById('login-form')
const baseEndpoint = 'http://localhost:8000/api_06'
const contentContainer = document.getElementById('content-container')
const searchForm = document.getElementById('search-form')
if (loginForm) {
  // handle this login form
  loginForm.addEventListener('submit', handleLogin)
}
if (searchForm) {
  // handle this search form
  searchForm.addEventListener('submit', handleSearch)
}

function handleLogin (event) {
  event.preventDefault()
  console.log(event)
  const loginEndpoint = `${baseEndpoint}/token/`
  let loginFormData = new FormData(loginForm)
  let loginObjectData = Object.fromEntries(loginFormData)
  let bodyStr = JSON.stringify(loginObjectData)
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: bodyStr
  }
  fetch(loginEndpoint, options) // requests.posts
  .then(response => {
    console.log(response)
    return response.json()
  })
  .then(authData => {
    handleAuthData(authData, getProductList)
  })
  .catch(err => {
    console.log(err)
  })
}

const handleAuthData = (authData, callback) => {
  localStorage.setItem('access', authData.access)
  localStorage.setItem('refresh', authData.access)
  if (callback) {
    callback()
  }
}

const getProductList = () => {
  const endpoint = `${baseEndpoint}/products_20/`
  const options = getFetchOptions()
  fetch(endpoint, options)
    .then(response => {
      return response.json()
    })
    .then(data => {
      const validData = isTokenNotValid(data)
      if (validData) {
        writeToContainer(data)
      }
    })
}

const writeToContainer = (data) => {
  if (contentContainer) {
    contentContainer.innerHTML = '<pre>' + JSON.stringify(data, null, 4) + '</pre>'
  }
}

const getFetchOptions = (method, body) => {
  return {
    method: method === null ? 'GET' : method,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${localStorage.getItem('access')}`
    },
    body: body ? body : null
  }
}

const isTokenNotValid = (jsonData) => {
  if (jsonData.code && jsonData.code === 'token_not_valid') {
    // run a refresh token fetch
    alert('Please login again')
    return false
  }
  return true
}

const validateJWTToken = () => {
  // fetch 
  const endpoint = `${baseEndpoint}/token/verify/`
  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      token: localStorage.getItem('access')
    })
  }
  fetch(endpoint, options)
    .then(response => response.json())
    .then(x => {
      // console.log(x)
      // isTokenNotValid(x)
      // refresh token
    })
}

function handleSearch(event) {
  event.preventDefault()
  
  let formData = new FormData(searchForm)
  let data = Object.fromEntries(formData)
  let searchParams = new URLSearchParams(data)
  const endpoint = `${baseEndpoint}/search/20/?${searchParams}`
  const headers = {
    'Content-Type': 'application/json'
  }
  const authToken = localStorage.getItem('access')
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`
  }
  const options = {
    method: 'GET',
    headers: headers
  }
  fetch(endpoint, options) // requests.posts
  .then(response => response.json())
  .then(data => {
    const validData = isTokenNotValid(data)
    if (validData && contentContainer) {
      contentContainer.innerHTML = ''
      console.log(data)
      if (data && data.results) {
        let htmlStr = ''
        for (let result of data.results) {
          htmlStr += '<li>' + result.title + '</li>'
        }
        contentContainer.innerHTML = htmlStr
        if (data.results.length === 0) {
          contentContainer.innerHTML = '<p> No results found</p>'
        }
      } else {
        contentContainer.innerHTML = '<p> No results found</p>'
      }
    }
  })
  // .then(data => writeToContainer(data))
  .catch(err => console.log(err))
}

validateJWTToken()