import React from "react";
import {
  KanbanComponent,
  ColumnsDirective,
  ColumnDirective,
} from "@syncfusion/ej2-react-kanban";

import { kanbanData, kanbanGrid } from "../data/dummy";
import { Header } from "../components";

const Kanban = () => (
  <div className="m-2 md:m-10 mt-24 p-2 md:p-10 bg-white rounded-3xl">
    <KanbanComponent id="kanban" keyField="Status" dataSource={kanbanData}>
      <ColumnsDirective>
        <ColumnDirective headerText="4-kishilik" keyField="Open" maxCount={4} />
        <ColumnDirective headerText="3-kishilik" keyField="Open" maxCount={4} />
        <ColumnDirective headerText="3-kishilik" keyField="Open" maxCount={4} />
        <ColumnDirective headerText="3-kishilik" keyField="Open" maxCount={4} />
      </ColumnsDirective>
    </KanbanComponent>
  </div>
);

export default Kanban;
