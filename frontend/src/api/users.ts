import { axi } from './useAxios'

export const registerRequest = async (email: string, name: string, lastname: string, password: string) => {
    await axi.post("/users/register/", { email, name, lastname, password })
}

export const loginRequest = async (email: string, password: string) => {
    const res = await axi.post("/users/login/", {email, password})
    return res
}