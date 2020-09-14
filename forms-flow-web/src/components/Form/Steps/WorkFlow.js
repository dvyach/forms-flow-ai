import React from "react";
import {
  FormLabel,
  FormControlLabel,
  RadioGroup,
  Radio,
  Grid,
  CardContent,
  Card,
} from "@material-ui/core";
import Select from "react-dropdown-select";
import SaveNext from "./SaveNext";
import ProcessDiagram from "../../BPMN/ProcessDiagram";

const WorkFlow = (props) => {
  const {
    associateWorkFlow,
    changeWorkFlowStatus,
    populateDropdown,
    associateToWorkFlow,
    handleNext,
    handleBack,
    activeStep,
    steps,
    workflow,
  } = props;

  // function onShown() {
  //   console.log("diagram shown");
  // }

  // function onLoading() {
  //   console.log("diagram loading");
  // }

  // function onError(err) {
  //   console.log("failed to show diagram");
  // }

  return (
    <Grid container direction="row" justify="flex-start" alignItems="baseline">
      {/* <FormControl component="fieldset"> */}

      <Grid item xs={9} spacing={3}/>
      <Grid item xs={3} className="next-btn">
        <SaveNext
          handleBack={handleBack}
          handleNext={handleNext}
          activeStep={activeStep}
          steps={steps}
        />
      </Grid>
      <Grid item sm={20} xs={12} spacing={3}>
        <Card variant="outlined" className="card-overflow">
          <CardContent>
              <Grid item xs={9} spacing={3}>
              {/* <FormLabel component="legend"> */}
              <h5> Do you want to associate form with a workflow ?</h5> 
              {/* </FormLabel> */}
              <RadioGroup
                aria-label="gender"
                name="gender1"
                value={associateWorkFlow}
                onChange={changeWorkFlowStatus}
                row
              >
                <FormControlLabel
                  value="yes"
                  control={<Radio color="primary" />}
                  label="Yes"
                />
                <FormControlLabel
                  value="no"
                  control={<Radio color="primary" />}
                  label="No"
                />
              </RadioGroup>
            </Grid>

            {associateWorkFlow === "yes" && (
              <>
                <Grid item xs={9} spacing={3}>
                  <h5>Please select a process </h5>

                  <Select
                    options={populateDropdown()}
                    onChange={(item) => associateToWorkFlow(item)}
                    values={workflow && workflow.value ? [workflow] : []}
                  />
                </Grid>
                <br/>
                {workflow && workflow.value && (
                  <Grid item xs={9} spacing={3}>
                    <ProcessDiagram
                      process_key={workflow && workflow.value}

                      onLoading={onLoading}
                      onShown={onShown}
                      onError={onError}

                    />
                  </Grid>
                )}
              </>
            )}
            {/* </FormControl> */}
          </CardContent>
        </Card>
      </Grid>
    </Grid>
  );
};
export default WorkFlow;