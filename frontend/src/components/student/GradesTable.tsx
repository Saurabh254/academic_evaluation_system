import React, { useEffect, useState } from "react";
import { GetMyGrades } from "../../services/student";

const data = [
  {
    subject: {},
    cgpa: 6.54,
    semester: 1,
    id: 0,
    student_id: "string",
    created_at: "2024-11-17T16:07:00.205Z",
    updated_at: "2024-11-17T16:07:00.205Z",
  },
  {
    subject: {},
    cgpa: 6.3,
    semester: 2,
    id: 1,
    student_id: "string",
    created_at: "2024-11-17T16:07:00.205Z",
    updated_at: "2024-11-17T16:07:00.205Z",
  },
];

const GradesTable = () => {
  const [grades, SetGrades] = useState(null);
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
            <tr key={item.id}>
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

export default GradesTable;
