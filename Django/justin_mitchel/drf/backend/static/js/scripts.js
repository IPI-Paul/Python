const deleteItem = (e) => {
  e = e || window.event
  e.preventDefault()
  const target = e.target || e.srcElement
  const sibling = target.parentElement.parentElement.previousElementSibling
  const xhr = new XMLHttpRequest()
  const url = target.innerText
  if (confirm('You are about to delete this record.\n\n Do you want to continue?')) {
    xhr.open("DELETE", url, true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    cookie = ('; ' + document.cookie).split(`; csrftoken=`).pop().split(';')[0] | ''
    if (cookie !== '') {
      xhr.setRequestHeader('X-CSRFTOKEN', `${getCookie('csrftoken')}`)
    }
    xhr.send()
    setTimeout(() => {
      document.location.reload()
      sibling.focus()
    }, 500)
  }
}

const formElements = (formEl, obj) => {
  email = false
  Object.entries(obj).map(([k, v]) => {
    const group = document.createElement('div')
    const lbl = document.createElement('label')
    lbl.htmlFor = k
    lbl.innerHTML = toSentenceCase(k.replace(/_/g, ' '))
    group.appendChild(lbl)
    const el = !['body', 'content'].includes(k)
      ? document.createElement('input')
      : document.createElement('textarea')
    el.id = k
    el.name = k
    el.disabled = k === 'id'
    if (k === 'email') {
      email = true
      el.type = 'email'
    }
    if(k === 'price') el.className = 'numbers'
    group.appendChild(el)
    formEl.appendChild(group)
  })
  return email
}

const getCookie = (name) => {
  let cookieValue = null

  if (document.cookie && document.cookie != '') {
    let cookies = document.cookie.split(';')

    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim()

      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }

  return cookieValue
}

const loadContent = (e, obj, method) => {
  e = e || window.event
  e.preventDefault()
  const target = e.target || e.srcElement
  const wn = window.open(`http://localhost:8000${target.innerText}`, '_blank')
  setTimeout(() => {
    if (method === 'POST') {
    const content = wn.document.getElementById('id__content')
    content.innerHTML = JSON.stringify(obj, null, 2)
    } else if (method === 'PUT') {
      Object.entries(obj).map(([k, v]) => {
        wn.document.getElementsByName(k)[0].value = `${v}`
      })
    }
  }, 250)
}

const postForm = (e, obj) => {
  e = e || window.event
  e.preventDefault()
  const target = e.target || e.srcElement
  const post_form = document.createElement('form')
  post_form.id = 'post_form'
  post_form.method = 'POST'
  post_form.target = '_blank'
  post_form.action = `http://localhost:8000${target.innerText}/`
  post_form.hidden = true
  if (obj) formElements(post_form, obj)
  document.body.appendChild(post_form)
  if (obj) Object.entries(obj).map(([k, v]) => {
    document.getElementById(k).value = v
  })
  const token = getCookie('csrftoken')
  const csrf = document.createElement('input')
  csrf.type = 'hidden'
  csrf.name = 'csrfmiddlewaretoken'
  csrf.value = token
  post_form.appendChild(csrf)
  post_form.submit()
  document.body.removeChild(post_form)
}

const toggleView = (e) => {
  e = e || window.event
  const target = e.target.parentElement || e.srcElement.parentElement
  const toggler = target.childNodes[0]
  toggler.innerText = toggler.innerText === '+' 
    ? '-' 
    : '+'
  target.nextElementSibling.className = toggler.innerText === '-'
    ? 'visible'
    : 'hidden'
  let vis = []
  for (let app_name of document.getElementsByClassName('app-name')) {
    if (app_name.nextElementSibling.className === 'visible') {
      vis.push(app_name.getAttribute('name'))
    }
  }
  localStorage.setItem('drf_visibles', vis.join(','))
}

const toSentenceCase = (str) => (
  str.replace(
    /\w\S*/g, (txt) => (txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase())
  )
)

const updateItem = (e, obj, css) => {
  delete obj['id']
  e = e || window.event
  e.preventDefault()
  const target = e.target || e.srcElement
  const reqForm = document.createElement('form')
  reqForm.className = 'update-form'
  reqForm.id = 'reqForm'
  const email = formElements(reqForm, obj)
  const group = document.createElement('div')
  group.id = 'submit'
  const el = document.createElement('button')
  el.innerText = 'Update'
  el.addEventListener('click', (e) => {
    e = e || window.event
    e.preventDefault()
    if (email && wn.document.getElementById('email').value === '') {
      alert('Email field must be filled in!')
      return
    }
    const data = JSON.stringify(Object.fromEntries(new FormData(wn.document.querySelector('form'))))
    const url = `http://localhost:8000${target.innerText}`
    const xhr = new XMLHttpRequest()
    xhr.open("PUT", url, true)
    xhr.setRequestHeader('Content-Type', 'application/json')
    cookie = ('; ' + document.cookie).split(`; csrftoken=`).pop().split(';')[0] | ''
    if (cookie !== '') {
      // xhr.setRequestHeader('Authorization', `Bearer ${token}`)
      xhr.setRequestHeader('X-CSRFTOKEN', `${getCookie('csrftoken')}`)
    }
    xhr.onload = (e) => {
      if (xhr.responseText.search('Error:') > 0) alert(xhr.responseText)
    }
    xhr.send(data)
    setTimeout(() => {
      wn.opener.location.reload()
      wn.close()
    }, 500)
  })
  group.appendChild(el)
  reqForm.appendChild(group)
  const styles = document.createElement('link')
  styles.href = `http://localhost:8000${css}`
  styles.rel = 'stylesheet'
  const wn = window.open('', '', 'height=350, width=400, toolbar=0')
  wn.document.head.appendChild(styles)
  wn.document.body.appendChild(reqForm)
  wn.document.body.className = 'body'
  Object.entries(obj).map(([k, v]) => {
    wn.document.getElementById(k).value = v
  })
}

const visCheck = () => {
  const vis = localStorage.getItem('drf_visibles')
  if (vis) {
    for (let app of document.getElementsByClassName('app-name')) {
      app.childNodes[0].innerText = '+'
      app.nextElementSibling.className = 'hidden'
    }
    for (let app_name of vis.split(',')) {
      for (let app of document.getElementsByClassName('app-name')) {
        if (app_name === app.getAttribute('name')) {
          app.childNodes[0].innerText = '-'
          app.nextElementSibling.className = 'visible'
        } 
      }
    }
  }
}

window.onload = setTimeout(
  () => {visCheck()},
  250
)