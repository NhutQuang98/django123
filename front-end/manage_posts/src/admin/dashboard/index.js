import React from 'react';
import Menu from './menu/Menu';
import TotalInfo from './totalInfo/TotalInfo';

function Dashboard() {
  return (
    <div style={{ display: 'flex' }}>
      <Menu />
      <TotalInfo name="User" amount="5" />
      <TotalInfo name="Posts" amount="2" />
    </div>
  );
}

export default Dashboard;