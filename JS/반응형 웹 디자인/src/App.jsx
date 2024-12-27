// import React from "react";
import styled from 'styled-components';
import Navbar from "./components/Navbar";

const GridContainer = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 16px;
  padding: 16px;
`;

const GridItem = styled.div`
  background-color: #f0f0f0;
  border: 1px solid #ddd;
  padding: 20px;
  text-align: center;
`;

const FormContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
`;

const InputGroup = styled.div`
  flex: 1;
  min-width: 200px;
`;

const SubmitButton = styled.button`
  padding: 10px 20px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
`;
const Hero = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 50px;
  text-align: center;
  background: url('hero-desktop.jpg') no-repeat center/cover;
  height: 300px;

  @media (max-width: 768px) {
    background: url('hero-mobile.jpg') no-repeat center/cover;
    height: 200px;
  }
`;
const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const TableHeader = styled.th`
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
`;

const TableRow = styled.tr`
  @media (max-width: 768px) {
    display: block;
    margin-bottom: 15px;
  }
`;

const TableCell = styled.td`
  @media (max-width: 768px) {
    text-align: right;
    position: relative;
    padding-left: 50%;
  }

  @media (max-width: 768px) {
    &:before {
      content: attr(data-label);
      position: absolute;
      left: 0;
      width: 45%;
      padding-left: 10px;
      font-weight: bold;
      text-align: left;
    }
  }
`;

const Gallery = styled.div`
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 10px;
`;

const GalleryImage = styled.img`
  width: 100%;
  border-radius: 5px;
`;
const App = () => {
  return (
    <div>
      <Navbar />
      <main>
        <Hero>
          <h1>Welcome to Our Website</h1>
          <p>Your journey starts here!</p>
        </Hero>
        <GridContainer>
          <GridItem>Item 1</GridItem>
          <GridItem>Item 2</GridItem>
          <GridItem>Item 3</GridItem>
          <GridItem>Item 4</GridItem>
        </GridContainer>
        <FormContainer>
          <InputGroup>
            <label htmlFor="name">Name</label>
            <input type="text" id="name" />
          </InputGroup>
          <InputGroup>
            <label htmlFor="email">Email</label>
            <input type="email" id="email" />
          </InputGroup>
          <SubmitButton type="submit">Submit</SubmitButton>
        </FormContainer>
        <Table>
          <thead>
            <tr>
              <TableHeader>Name</TableHeader>
              <TableHeader>Age</TableHeader>
              <TableHeader>City</TableHeader>
            </tr>
          </thead>
          <tbody>
            <TableRow>
              <TableCell data-label="Name">Alice</TableCell>
              <TableCell data-label="Age">25</TableCell>
              <TableCell data-label="City">New York</TableCell>
            </TableRow>
            <TableRow>
              <TableCell data-label="Name">Bob</TableCell>
              <TableCell data-label="Age">30</TableCell>
              <TableCell data-label="City">San Francisco</TableCell>
            </TableRow>
          </tbody>
        </Table>
        <Gallery>
          <GalleryImage src="image1.jpg" alt="Image 1" />
          <GalleryImage src="image2.jpg" alt="Image 2" />
          <GalleryImage src="image3.jpg" alt="Image 3" />
        </Gallery>
      </main>
    </div>
  );
};

export default App;
