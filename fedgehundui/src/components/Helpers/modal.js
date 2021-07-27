import React, { useState } from "react";
import { Modal, Button } from "react-bootstrap";

function ModalOnPageLoad() {
	const [showModal, setShow] = useState(true);

	const handleClose = () => setShow(false);

	return (
		<>
			<Modal
				show={showModal}
				onHide={handleClose}
				backdrop="static"
				keyboard={false}
				size="lg"
				aria-labelledby="contained-modal-title-vcenter"
				centered
			>
				<Modal.Header closeButton>
					<Modal.Title style={{ padding: "8px" }}>
						<i className="fas fa-tools" style={{ marginRight: "10px" }}></i> Welcome
					</Modal.Title>
				</Modal.Header>
				<Modal.Body>
					<p style={{ paddingLeft: "8px", paddingTop: "15px" }}>
						This website is currently under development. Some of the features may not work properly.
						<br />
						<br />
						We apologize for the inconvenience.
					</p>
				</Modal.Body>
				<Modal.Footer>
					<Button variant="secondary" onClick={handleClose} style={{ marginRight: "6px", width: "80px" }}>
						Close
					</Button>
				</Modal.Footer>
			</Modal>
		</>
	);
}

export default ModalOnPageLoad;
