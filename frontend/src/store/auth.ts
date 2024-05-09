import { create } from "zustand";
import { persist } from "zustand/middleware";

type State = {
    access: String;
    refresh: String;
    isAuth: Boolean;
}

type Actions = {
    setToken: (access: String, refresh: string) => void;
    logout: () => void;
}

export const useAuthStore = create(
    persist<State & Actions>(
        (set) => ({
            access: '',
            refresh: '',
            isAuth: false,
            setToken: (access: String, refresh: String) =>
                set(() => ({
                    access,
                    refresh,
                    isAuth: !!access && !!refresh,
                })),
            logout: () => set(() => ({ access: '', refresh: '', isAuth: false })),
        }),
        {
            name: 'Auth'
        }
    )
)