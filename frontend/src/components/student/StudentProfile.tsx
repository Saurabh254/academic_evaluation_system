import React, { useEffect, useState } from "react";
import GradesTable from "./GradesTable";
import { GetMyGrades, GetStudent } from "../../services/student";

const StudentProfile = ({ student }) => {
  return (
    <div className="flex  items-center my-8 w-full">
      <div className="w-full  rounded-lg  p-6 flex justify-evenly [&>*]:w-1/2">
        <div className="flex justify-center mb-6">
          <img
            src="/logo.png"
            alt="Profile"
            className="rounded-lg object-cover"
          />
        </div>
        <table className="w-full">
          <tbody>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Enrollment ID:
              </td>
              <td className="py-2 text-gray-800">{student.id}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">Name:</td>
              <td className="py-2 text-gray-800">{student.name}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Current Semester:
              </td>
              <td className="py-2 text-gray-800">{student.semester}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">Email:</td>
              <td className="py-2 text-gray-800">{student.email}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">Address:</td>
              <td className="py-2 text-gray-800">{student.address}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Father's Name:
              </td>
              <td className="py-2 text-gray-800">{student.father_name}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Mother's Name:
              </td>
              <td className="py-2 text-gray-800">{student.mother_name}</td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Registered At:
              </td>
              <td className="py-2 text-gray-800">
                {new Date(student.created_at).toLocaleString()}
              </td>
            </tr>
            <tr>
              <td className="py-2 font-semibold text-gray-600">
                Profile Modified At:
              </td>
              <td className="py-2 text-gray-800">
                {new Date(student.updated_at).toLocaleString()}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

const App = () => {
  const [student, SetStudent] = useState(null);

  useEffect(() => {
    const call_api = async () => {
      const student = await GetStudent();
      SetStudent(student.data);
    };
    call_api();
  }, []);
  if (student == null) {
    return <span className="flex items-center justify-center">loading...</span>;
  }
  return (
    <>
      <h1 className="text-xl text-center w-full pl-12 pt-6 font-bold mb-6">
        {student.name} Profile
      </h1>
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <StudentProfile student={student} />
      <h3 className="mb-2">Recent Grades</h3>
      <hr className="border-b-2 border-gray-200 w-full mb-4" />
      <GradesTable />
    </>
  );
};

export default App;
