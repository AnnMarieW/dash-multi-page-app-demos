
var dagcomponentfuncs = window.dashAgGridComponentFunctions = window.dashAgGridComponentFunctions || {};

dagcomponentfuncs.StockLink = function (props) {
    return React.createElement(window.dash_core_components.Link, {
        children: props.value,
        href: '/stocks/' + props.data.ticker,
    });
}