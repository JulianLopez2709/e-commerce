import { BrowserRouter, Route, Routes } from 'react-router-dom'
import { AdminPrivateRoute, PrivateRoute } from './components/PrivateRoute'
import Layout from "./components/Layout"
import HomePage from './page/HomePage'
import LoginPage from './page/LoginPage'
import RegisterPage from './page/RegisterPage'
import AdminPage from './page/AdminPage'
import AddProductPage from './page/AddProductPage'

AdminPage

function App() {

  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Layout />}>
            <Route index element={<HomePage />}></Route>
            <Route path='login' element={<LoginPage />}/>
            <Route path='register' element={<RegisterPage />}/>

            <Route element={<PrivateRoute />}>

            </Route>

            <Route path='admin' element={<AdminPrivateRoute />}>
              <Route index element={<AdminPage />}/>
              <Route path='add' element={<AddProductPage />}/>
            </Route>

          </Route>
        </Routes>
      </BrowserRouter>
    </>
  )
}

export default App
