import { axi } from './useAxios'

export const registerRequest = async (email: String, name: String, lastname: String, password: String) => {
    await axi.post("/users/register/", { email, name, lastname, password })
}

export const loginRequest = async (email: String, password: String) => {
    const res = await axi.post("/users/login/", { email, password })
    return res
}