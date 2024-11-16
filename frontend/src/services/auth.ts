import { useNavigate } from "react-router-dom";
import { LoginUser } from "../api/login_signup";
import { FormData } from "../types/auth";

export const HandleUserLogin = async (credentials: FormData) => {
  const request_body = {
    username: credentials.identity,
    password: credentials.password,
  };
  return await LoginUser(request_body);
};
