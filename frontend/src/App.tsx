import { useState } from 'react'
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import  Layout from "./components/Layout"
import HomePage from './page/HomePage'
import LoginPage from './page/LoginPage'
import RegisterPage from './page/RegisterPage'
import AdminPage from './page/AdminPage'

AdminPage

function App() {

  return (
    <>
      <BrowserRouter>
          <Routes>
            <Route path='/' element={<Layout/>}>
              <Route index element={<HomePage/>}></Route>
              <Route path='/login' element={<LoginPage/>}></Route>
              <Route path='/register' element={<RegisterPage/>}></Route>
              <Route path='/admin' element={<AdminPage/>}></Route>
            </Route>
          </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
