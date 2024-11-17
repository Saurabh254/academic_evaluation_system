import React, { useEffect, useState } from "react";
import { Chart } from "react-google-charts";
import GradesTable from "./GradesTable";
import { GetMyGrades } from "../../services/student";

interface Grade {
  grate: object;
}

const parse_data_with_colors = (data) => {
  const parsed_data = [];
  parsed_data.push(["Subject", "Marks", { role: "style" }]);
  for (const item of data) {
    let marks = 0;
    if (item.marks == "a+") {
      marks = 100;
    } else if (item.marks == "a") {
      marks = 95;
    } else {
      marks = 50;
    }
    parsed_data.push([item.subject, marks, "color: green"]);
  }
  console.log(parsed_data);
  return parsed_data;
};
const ColumnChart = ({ grade }: Grade) => {
  const parsed_data = parse_data_with_colors(grade.grades);
  console.log(parsed_data);
  const options = {
    title: `Marks of ${grade.semester} semster`,
    chartArea: { width: "100%" },
    hAxis: {
      title: "Marks",
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
  const [grades, SetGrades] = useState(null);
  useEffect(() => {
    const call_api = async () => {
      const grades = await GetMyGrades();
      SetGrades(grades.data);
    };
    call_api();
  }, []);
  if (grades == null) {
    return <h1>loading...</h1>;
  }
  return (
    <>
      <div className="flex justify-evenly w-full flex-wrap ">
        {grades.map((grade) => {
          return <ColumnChart grade={grade} />;
        })}
      </div>
    </>
  );
};
export default GradeChart;
