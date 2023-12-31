import axios from 'axios'
import {
  SPREADSHEET_LIST_REQUEST,
  SPREADSHEET_LIST_SUCCESS,
  SPREADSHEET_LIST_FAIL,
  SPREADSHEET_DETAILS_REQUEST,
  SPREADSHEET_DETAILS_SUCCESS,
  SPREADSHEET_DETAILS_FAIL
} from '../constants/spreadsheetConstants'

export const listSpreadsheets = () => async (dispatch) => {
  try {
    dispatch({
      type: SPREADSHEET_LIST_REQUEST
    })
    const {data} = await axios.get(`/spreadsheets`)
    dispatch({
      type: SPREADSHEET_LIST_SUCCESS,
      payload: data
    })
  } catch (error) {
    dispatch({
      type: SPREADSHEET_LIST_FAIL,
      payload: error.response && error.response.data.message ? error.response.data.message : error.message
    })
  }
}

export const listSpreadsheetDetails = (id) => async (dispatch) => {
  try {
    dispatch({
      type: SPREADSHEET_DETAILS_REQUEST
    })
    const {data} = await axios.get(`/spreadsheets/${id}`)
    dispatch({
      type: SPREADSHEET_DETAILS_SUCCESS,
      payload: data
    })
  } catch (error) {
    dispatch({
      type: SPREADSHEET_DETAILS_FAIL,
      payload: error.response && error.response.data.message ? error.response.data.message : error.message
    })
  }
}