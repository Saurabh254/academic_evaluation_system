import { useEffect, useState } from "react";
import GradesTable, { GradesView } from "../student/GradesTable";
import { StudentProfile } from "../student/StudentProfile";
import { Student } from "@/types/student";
import { FetchGradeByStudentId, FetchStudentById } from "@/api/login_signup";
import { useNavigate, useParams } from "react-router-dom";
import { StudentGrade } from "@/types/grades";
import Charts from "./Charts";

const StudentView = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  if (id == undefined) {
    navigate("/teacher");
  }
  const [student, setStudent] = useState<Student | null>(null);
  const [grades, setGrades] = useState<StudentGrade[] | []>([]);
  useEffect(() => {
    const call_api = async () => {
      let response = await FetchStudentById(id);
      if (response.status == 200) {
        setStudent(response.data);
      }
      response = await FetchGradeByStudentId(id);
      if (response.status == 200) {
        setGrades(response.data);
      }
    };
    call_api();
  }, []);

  if (student == null) {
    return <h1>Loading...</h1>;
  }
  return (
    <>
      <h1 className="text-xl text-center w-full pl-12 pt-6 font-bold mb-6">
        {student.name} Profile
      </h1>
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <StudentProfile student={student} />
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <h3 className="mb-2">Recent Grades</h3>
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <GradesView grades={grades} />
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <h3 className="mb-2">Grades Visualization</h3>
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <Charts grades={grades} />
      <span className="mb-24"></span>
    </>
  );
};

export default StudentView;
