import { LoginTeacher, LoginUser } from "../api/login_signup";
import { FormData } from "../types/auth";

interface Credentials {
  username: string;
  password: string;
}

export const HandleUserLogin = async (credentials: Credentials) => {
  const request_body = {
    username: credentials.username,
    password: credentials.password,
  };
  return await LoginUser(request_body);
};
export const HandleTeacherLogin = async (credentials: Credentials) => {
  const request_body = {
    username: credentials.username,
    password: credentials.password,
  };
  return await LoginTeacher(request_body);
};



