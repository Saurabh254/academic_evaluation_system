import axios from "axios";
import apiClient, { apiClientNoAuth } from "../common/base_api";
import { LoginRequestBody } from "../types/auth";

export const LoginUser = async (request_body: LoginRequestBody) => {
  return await apiClientNoAuth.post(
    '/students/login', request_body
  )
};

// Fa0uU08DSMfa

export const FetchUser = async () => {
  return await apiClient.get('/students/me')
}

export const GetGrades = async () => {
  return await apiClient.get('/grades')
}