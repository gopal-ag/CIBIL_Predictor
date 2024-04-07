import { ResponsivePie } from "@nivo/pie"

const PieComp = ({
    data
}) => {
    return (
        <div className="h-64 w-1/4 ">
            <ResponsivePie
                data={data}
                margin={{ top: 40, right: 20, bottom: 40, left: 20 }}
                innerRadius={0.6}
                padAngle={0.5}
                cornerRadius={3}
                colors={{ scheme: 'dark2' }}
                activeOuterRadiusOffset={8}
                borderWidth={1}
                borderColor={{
                    from: 'color',
                    modifiers: [
                        [
                            'darker',
                            0.2
                        ]
                    ]
                }}
                arcLinkLabelsSkipAngle={10}
                arcLinkLabelsTextColor="#223241"
                arcLinkLabelsThickness={2}
                arcLinkLabelsColor={{ from: 'color' }}
                arcLabelsSkipAngle={10}
                arcLabelsTextColor={{
                    from: 'color',
                    modifiers: [
                        [
                            'darker',
                            10
                        ]
                    ]
                }}
            />
        </div>
    )
}

export default PieComp
