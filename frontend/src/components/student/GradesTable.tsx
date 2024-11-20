import React, { useEffect, useState } from "react";
import { GetMyGrades } from "../../services/student";
import { Grade, StudentGrade } from "../../types/grades";

interface GradeView {
  grades: StudentGrade[];
}

export const GradesView = ({ grades }: GradeView) => {
  if (grades == null || grades.length == 0) {
    return <span className="mb-4">no grades data available</span>;
  }
  return (
    <div className="overflow-x-auto w-full ml-44">
      <table className="table w-full">
        {/* Table Head */}
        <thead>
          <tr>
            <th>#</th>
            <th>CGPA</th>
            <th>Semester</th>
            <th>Created At</th>
            <th>Updated At</th>
          </tr>
        </thead>
        <tbody>
          {/* Dynamically Render Rows */}
          {grades.map((item, index) => (
            <tr key={`${item.id}-${index}`}>
              <th>{index + 1}</th>
              <td>{item.cgpa}</td>
              <td>{item.semester}</td>
              <td>{new Date(item.created_at).toLocaleString()}</td>
              <td>{new Date(item.updated_at).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
const GradesTable = () => {
  const [grades, SetGrades] = useState<StudentGrade[]>([]);
  useEffect(() => {
    const call_api = async () => {
      const grades = await GetMyGrades();
      if (grades.status != 404) {
        SetGrades(grades.data);
      }
    };
    call_api();
  }, []);
  if (grades == null) {
    return <span>record not available</span>;
  }
  return <GradesView grades={grades} />;
};

export default GradesTable;
