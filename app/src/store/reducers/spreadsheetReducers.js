import {
  SPREADSHEET_LIST_REQUEST,
  SPREADSHEET_LIST_SUCCESS,
  SPREADSHEET_LIST_FAIL,
  SPREADSHEET_DETAILS_REQUEST,
  SPREADSHEET_DETAILS_SUCCESS,
  SPREADSHEET_DETAILS_FAIL
} from '../constants/spreadsheetConstants'

export const spreadsheetListReducer = (state = {spreadsheets: [], count: 0}, action) => {
  switch (action.type) {
    case SPREADSHEET_LIST_REQUEST:
      return {
        loading: true
      }
    case SPREADSHEET_LIST_SUCCESS:
      return {
        loading: false,
        spreadsheets: action.payload.items,
        count: action.payload.count
      }
    case SPREADSHEET_LIST_FAIL:
      return {
        loading: false,
        error: action.payload
      }
    default:
      return state
  }
}

export const spreadsheetDetailsReducer = (state = {spreadsheet: {}}, action) => {
  switch (action.type) {
    case SPREADSHEET_DETAILS_REQUEST:
      return {
        loading: true
      }
    case SPREADSHEET_DETAILS_SUCCESS:
      return {
        loading: false,
        count: action.payload.count,
        items: action.payload.items
      }
    case SPREADSHEET_DETAILS_FAIL:
      return {
        loading: false,
        error: action.payload
      }
    default:
      return state
  }
}