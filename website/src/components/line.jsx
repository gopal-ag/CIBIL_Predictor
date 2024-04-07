import { ResponsiveLine } from "@nivo/line"

const LineComp = ({
    data
}) => {
    return (
        <div className="h-64 w-full">
            <ResponsiveLine
                data={data}
                margin={{ top: 50, right: 20, bottom: 40, left: 50 }}
                colors={{ scheme: 'dark2' }}
                xScale={{ type: 'point' }}
                yScale={{
                    type: 'linear',
                    min: 'auto',
                    max: 'auto',
                    stacked: true,
                    reverse: false
                }}
                yFormat=" >-.2f"
                axisTop={null}
                axisRight={null}
                axisBottom={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'transportation',
                    legendOffset: 36,
                    legendPosition: 'middle',
                    truncateTickAt: 0
                }}
                axisLeft={{
                    tickSize: 5,
                    tickPadding: 5,
                    tickRotation: 0,
                    legend: 'count',
                    legendOffset: -40,
                    legendPosition: 'middle',
                    truncateTickAt: 0
                }}
                pointSize={10}
                pointColor={{ theme: 'background' }}
                pointBorderWidth={2}
                pointBorderColor={{ from: 'serieColor' }}
                pointLabelYOffset={-12}
                enableTouchCrosshair={true}
                useMesh={true} />
        </div>
    )
}

export default LineComp
