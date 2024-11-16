import axios from "axios";
import apiClient from "../common/base_api";
import { LoginRequestBody } from "../types/auth";


export const LoginUser = async (request_body: LoginRequestBody) => {
    try {
        const response = await axios.post('/login', request_body);
        return response;
    } catch (error) {
        throw new Error(`Got error while calling /login: ${error}`);
    }
}