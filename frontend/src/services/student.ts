import { FetchStudentList } from "@/api/student";
import { FetchGradeByStudentId, FetchStudentById, FetchUser, GetGrades } from "../api/login_signup";

export const GetStudent = async () => {

    return await FetchUser();
};


export const GetMyGrades = async () => {
    return await GetGrades();
}

export const ListStudents = async () => {
    return await FetchStudentList();
}

export const GetStudentById = async (student_id: string) => {
    return await FetchStudentById(student_id);
}

export const GetGradeByStudentId = async (student_id: string) => {
    return await FetchGradeByStudentId(student_id);
}