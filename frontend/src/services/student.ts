import { FetchUser, GetGrades } from "../api/login_signup";

export const GetStudent = async () => {

    return await FetchUser();
};


export const GetMyGrades = async () => {
    return await GetGrades();
}