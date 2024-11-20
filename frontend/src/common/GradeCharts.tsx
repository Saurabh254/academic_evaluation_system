import React, { lazy, useEffect, useState, Suspense } from "react";
import { Chart } from "react-google-charts";

// Lazy load the GetMyGrades function

import { Grade, StudentGrade } from "../types/grades";
import { GetMyGrades } from "../services/student";

const parse_data_with_colors = (data: Grade[]) => {
  const parsed_data = [];
  parsed_data.push(["Subject", "Marks", { role: "style" }]);
  for (const item of data) {
    parsed_data.push([item.subject, item.marks, "color: green"]);
  }
  return parsed_data;
};

interface ColumnChartType {
  student_grade: StudentGrade;
}

export const ColumnChart = ({ student_grade }: ColumnChartType) => {
  const parsed_data = parse_data_with_colors(student_grade.grades);
  const options = {
    title: `Marks of ${student_grade.semester} semester - CGPA ${student_grade.cgpa}`,
    chartArea: { width: "100%" },
    hAxis: {
      title: `Marks of ${student_grade.semester} : Updated At ${new Date(
        student_grade.created_at
      ).toDateString()}`,
      minValue: 0,
    },
    vAxis: {
      title: "Subject",
    },
  };

  return (
    <div>
      <Chart
        chartType="ColumnChart"
        width="400px"
        height="400px"
        data={parsed_data}
        options={options}
      />
    </div>
  );
};

const GradeChart = () => {
  const [studentGrades, setStudentGrades] = useState<StudentGrade[]>([]);
  const [loading, setLoading] = useState(true); // Add loading state

  useEffect(() => {
    const call_api = async () => {
      const grades = await GetMyGrades();
      setStudentGrades(grades.data);
      setLoading(false); // Set loading to false after data is fetched
    };
    call_api();
  }, []);

  // Show loading message while data is being fetched
  if (loading) {
    return <h1>Loading...</h1>;
  }

  return (
    <>
      <div className="flex justify-evenly w-full flex-wrap">
        {studentGrades.map((grades: StudentGrade, index: number) => {
          return (
            <ColumnChart
              student_grade={grades}
              key={grades.student_id + "-" + grades.semester}
            />
          );
        })}
      </div>
    </>
  );
};

// Wrap GradeChart with Suspense
const GradeChartWithSuspense = () => (
  <Suspense fallback={<h1>Loading grades...</h1>}>
    <GradeChart />
  </Suspense>
);

export default GradeChartWithSuspense;
