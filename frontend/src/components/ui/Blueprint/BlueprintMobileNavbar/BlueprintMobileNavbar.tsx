/** The mobile navbar of the data management application. */
import Link from 'next/link';
import { useState } from 'react';
import {
  Alignment,
  AnchorButton,
  Button,
  Drawer,
  Classes,
} from '@blueprintjs/core';

export const BlueprintMobileNavbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const handleOpen = () => setIsOpen(true);

  const handleClose = () => setIsOpen(false);

  return (
    <>
      <Button
        type="button"
        rightIcon="menu"
        minimal={true}
        onClick={handleOpen}
      />
      <Drawer
        className={Classes.DARK}
        title="404"
        isOpen={isOpen}
        onClose={handleClose}
        size="320px"
      >
        <div className={Classes.DRAWER_BODY}>
          <Link href="/home" passHref={true}>
            <AnchorButton
              text="Home"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
          <Link href="/employees" passHref={true}>
            <AnchorButton
              text="Employees"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
          <Link href="/warehouses" passHref={true}>
            <AnchorButton
              text="Warehouses"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
          <Link href="/orders" passHref={true}>
            <AnchorButton
              text="Orders"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
          <Link href="/customers" passHref={true}>
            <AnchorButton
              text="Customers"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
          <Link href="/suppliers" passHref={true}>
            <AnchorButton
              text="Suppliers"
              alignText={Alignment.LEFT}
              minimal={true}
              onClick={handleClose}
            />
          </Link>
        </div>
      </Drawer>
    </>
  );
};