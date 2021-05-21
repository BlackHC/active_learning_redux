store = {}
store['timestamp']=1621483462
store['cmdline']=['/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py', '--id=75']
store['commit']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['github_url']='8a2cf4fb40ce306533b4e439b08268c53f009a3b'
store['experiment']='/home/kell4989/git/active_learning_redux/batchbald_redux/ood_experiment.py'
store['job_id']=75
store['worker_id']=75
store['num_workers']=80
store['config']={'seed': 1313, 'uniform_ood': False, 'id_dataset_type': 'batchbald_redux.fast_mnist.FastFashionMNIST', 'ood_dataset_type': 'batchbald_redux.fast_mnist.FastMNIST', 'initial_training_set_size': 20, 'validation_set_size': 1024, 'evaluation_set_size': 16, 'id_repetitions': 1, 'ood_repetitions': 1, 'add_dataset_noise': False, 'validation_split_random_state': 0, 'acquisition_size': 5, 'max_training_set': 200, 'num_pool_samples': 100, 'num_validation_samples': 20, 'num_training_samples': 1, 'num_patience_epochs': 3, 'max_training_epochs': 30, 'training_batch_size': 64, 'device': 'cuda', 'min_samples_per_epoch': 5056, 'acquisition_function': 'batchbald_redux.acquisition_functions.BatchBALD', 'train_eval_model': 'batchbald_redux.train_eval_model.TrainSelfDistillationEvalModel', 'model_optimizer_factory': 'batchbald_redux.models.MnistOptimizerFactory', 'acquisition_function_args': None, 'temperature': 8}
store['log']={}
store['dataset_info']={'training': "(FastFashionMNIST (train; 58976 samples)) + ('FastMNIST Train (60000 samples)' | constant_target{'target': tensor(-1, device='cuda:0'), 'num_classes': 10})", 'test': "'FastFashionMNIST Test (10000 samples)'"}
store['initial_training_set_indices']=[55573, 380, 12640, 44119, 30392, 58226, 43812, 52440, 3091, 29974, 49512, 46037, 53434, 22015, 37915, 52296, 8533, 58125, 22304, 35472]
store['evaluation_set_indices']=[42890, 14640, 45567, 52801, 53689, 801, 55187, 26479, 50997, 3792]
store['active_learning_steps']=[]
store['active_learning_steps'].append({})
store['active_learning_steps'][0]['training']={}
store['active_learning_steps'][0]['training']['epochs']=[]
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.6479835510253906})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.16768741607666})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.443005084991455})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.411048412322998})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.782407760620117})
store['active_learning_steps'][0]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.928966522216797})
store['active_learning_steps'][0]['training']['best_epoch']=3
store['active_learning_steps'][0]['evaluation_metrics']={'accuracy': 0.6065, 'crossentropy': 3.357883203125}
store['active_learning_steps'][0]['acquisition']={'indices': [['id', 59392], ['id', 22505], ['id', 55778], ['id', 41713], ['id', 59228]], 'labels': [-1, -1, 8, -1, -1], 'scores': [1.4929251546887286, 2.7311346017628058, 3.5567961953130336, 4.070482613050222, 4.347795608172749]}
store['active_learning_steps'].append({})
store['active_learning_steps'][1]['training']={}
store['active_learning_steps'][1]['training']['epochs']=[]
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.69107985496521})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1175155639648438})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.631646156311035})
store['active_learning_steps'][1]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.7552056312561035})
store['active_learning_steps'][1]['training']['best_epoch']=1
store['active_learning_steps'][1]['evaluation_metrics']={'accuracy': 0.5756, 'crossentropy': 2.6577}
store['active_learning_steps'][1]['acquisition']={'indices': [['id', 18092], ['id', 54805], ['id', 35158], ['id', 34097], ['id', 18564]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3645949581571255, 2.360982312824137, 3.1704651393232304, 3.701467698328905, 4.043869486793021]}
store['active_learning_steps'].append({})
store['active_learning_steps'][2]['training']={}
store['active_learning_steps'][2]['training']['epochs']=[]
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.1176772117614746})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.835268020629883})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.919424533843994})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.6332778930664062})
store['active_learning_steps'][2]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.217487335205078})
store['active_learning_steps'][2]['training']['best_epoch']=2
store['active_learning_steps'][2]['evaluation_metrics']={'accuracy': 0.6153, 'crossentropy': 2.953196484375}
store['active_learning_steps'][2]['acquisition']={'indices': [['id', 52372], ['id', 49896], ['id', 30341], ['id', 125], ['id', 1376]], 'labels': [-1, -1, -1, 2, -1], 'scores': [1.4539771522776643, 2.512781251335166, 3.337075410132467, 3.853281819648058, 4.173750749250389]}
store['active_learning_steps'].append({})
store['active_learning_steps'][3]['training']={}
store['active_learning_steps'][3]['training']['epochs']=[]
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.967137098312378})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.512974739074707})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9771065711975098})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.411734104156494})
store['active_learning_steps'][3]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.441431999206543})
store['active_learning_steps'][3]['training']['best_epoch']=2
store['active_learning_steps'][3]['evaluation_metrics']={'accuracy': 0.6156, 'crossentropy': 2.75533359375}
store['active_learning_steps'][3]['acquisition']={'indices': [['id', 28713], ['id', 19947], ['id', 26477], ['id', 41945], ['id', 34676]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.532722700576734, 2.5969899226840827, 3.4183417088764756, 3.9641561453013514, 4.264628144856593]}
store['active_learning_steps'].append({})
store['active_learning_steps'][4]['training']={}
store['active_learning_steps'][4]['training']['epochs']=[]
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.093055009841919})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.853926658630371})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.1306891441345215})
store['active_learning_steps'][4]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 2.959141492843628})
store['active_learning_steps'][4]['training']['best_epoch']=1
store['active_learning_steps'][4]['evaluation_metrics']={'accuracy': 0.5874, 'crossentropy': 2.5150958984375}
store['active_learning_steps'][4]['acquisition']={'indices': [['id', 33836], ['id', 19385], ['id', 39442], ['id', 15927], ['id', 50441]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5536851410436463, 2.6349239410892866, 3.379509043299694, 3.864497108596643, 4.1778652931692735]}
store['active_learning_steps'].append({})
store['active_learning_steps'][5]['training']={}
store['active_learning_steps'][5]['training']['epochs']=[]
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.2048091888427734})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6857099533081055})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.717437267303467})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.9110121726989746})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 2.9683656692504883})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.2318201065063477})
store['active_learning_steps'][5]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.813361644744873})
store['active_learning_steps'][5]['training']['best_epoch']=4
store['active_learning_steps'][5]['evaluation_metrics']={'accuracy': 0.629, 'crossentropy': 3.10599609375}
store['active_learning_steps'][5]['acquisition']={'indices': [['id', 31360], ['id', 2773], ['id', 54511], ['id', 13309], ['id', 51730]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.689457400461984, 2.8757395896089024, 3.7421019016951362, 4.20834988619337, 4.427310526596955]}
store['active_learning_steps'].append({})
store['active_learning_steps'][6]['training']={}
store['active_learning_steps'][6]['training']['epochs']=[]
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.084282875061035})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9669227600097656})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.1156558990478516})
store['active_learning_steps'][6]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.9697346687316895})
store['active_learning_steps'][6]['training']['best_epoch']=1
store['active_learning_steps'][6]['evaluation_metrics']={'accuracy': 0.6064, 'crossentropy': 2.2796115234375}
store['active_learning_steps'][6]['acquisition']={'indices': [['id', 32504], ['id', 5013], ['id', 3739], ['id', 7909], ['id', 58220]], 'labels': [-1, -1, -1, -1, 6], 'scores': [1.4251940572647002, 2.4326890988567493, 3.2547861641556857, 3.7885623336025223, 4.105899738731912]}
store['active_learning_steps'].append({})
store['active_learning_steps'][7]['training']={}
store['active_learning_steps'][7]['training']['epochs']=[]
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.3380675315856934})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 2.9347939491271973})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.58984375, 'crossentropy': 3.3977854251861572})
store['active_learning_steps'][7]['training']['epochs'].append({'accuracy': 0.580078125, 'crossentropy': 3.8806345462799072})
store['active_learning_steps'][7]['training']['best_epoch']=1
store['active_learning_steps'][7]['evaluation_metrics']={'accuracy': 0.5594, 'crossentropy': 2.558730859375}
store['active_learning_steps'][7]['acquisition']={'indices': [['id', 14260], ['id', 14129], ['id', 44737], ['id', 39545], ['id', 17045]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3943159734225743, 2.4502602808029774, 3.208997714164637, 3.755420878421586, 4.095460588226201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][8]['training']={}
store['active_learning_steps'][8]['training']['epochs']=[]
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 1.9745655059814453})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.5377626419067383})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.383054733276367})
store['active_learning_steps'][8]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9742565155029297})
store['active_learning_steps'][8]['training']['best_epoch']=1
store['active_learning_steps'][8]['evaluation_metrics']={'accuracy': 0.6157, 'crossentropy': 2.118859375}
store['active_learning_steps'][8]['acquisition']={'indices': [['id', 42934], ['id', 1116], ['id', 7909], ['id', 2676], ['id', 15140]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.437048612323134, 2.5239958143109744, 3.2739797548528617, 3.815025684494006, 4.140674691347396]}
store['active_learning_steps'].append({})
store['active_learning_steps'][9]['training']={}
store['active_learning_steps'][9]['training']['epochs']=[]
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.092623233795166})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.779644012451172})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.8013916015625})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.95267915725708})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1360697746276855})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3178884983062744})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.2051925659179688})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0834569931030273})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.34967041015625})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3421058654785156})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.365805149078369})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.702437162399292})
store['active_learning_steps'][9]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.786709785461426})
store['active_learning_steps'][9]['training']['best_epoch']=10
store['active_learning_steps'][9]['evaluation_metrics']={'accuracy': 0.5918, 'crossentropy': 3.602701953125}
store['active_learning_steps'][9]['acquisition']={'indices': [['id', 1646], ['id', 41277], ['id', 14129], ['id', 33520], ['id', 59747]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.569642955218833, 2.8472047920342214, 3.7110410028288747, 4.189687954356612, 4.435042436928018]}
store['active_learning_steps'].append({})
store['active_learning_steps'][10]['training']={}
store['active_learning_steps'][10]['training']['epochs']=[]
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.0385048389434814})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8252596855163574})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6703577041625977})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.1406588554382324})
store['active_learning_steps'][10]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.0209832191467285})
store['active_learning_steps'][10]['training']['best_epoch']=2
store['active_learning_steps'][10]['evaluation_metrics']={'accuracy': 0.6153, 'crossentropy': 2.901359765625}
store['active_learning_steps'][10]['acquisition']={'indices': [['id', 37815], ['id', 29380], ['id', 5013], ['id', 25627], ['id', 23381]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5900513225010275, 2.7867047964187086, 3.62819403286003, 4.1203391120270165, 4.376478479720813]}
store['active_learning_steps'].append({})
store['active_learning_steps'][11]['training']={}
store['active_learning_steps'][11]['training']['epochs']=[]
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.5859375, 'crossentropy': 2.257591485977173})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 2.634951114654541})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6005859375, 'crossentropy': 2.876854419708252})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.7934470176696777})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.509861469268799})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.603515625, 'crossentropy': 3.5404436588287354})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.6461973190307617})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1790502071380615})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.6412763595581055})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 4.111093044281006})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.609837532043457})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 4.0372443199157715})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.512828826904297})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1886281967163086})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.360187530517578})
store['active_learning_steps'][11]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.444347381591797})
store['active_learning_steps'][11]['training']['best_epoch']=13
store['active_learning_steps'][11]['evaluation_metrics']={'accuracy': 0.5987, 'crossentropy': 3.995746875}
store['active_learning_steps'][11]['acquisition']={'indices': [['id', 54805], ['id', 14129], ['id', 1392], ['id', 18383], ['id', 4399]], 'labels': [-1, -1, -1, -1, 1], 'scores': [1.560522255824526, 2.800805240596235, 3.7223833815137617, 4.198677408432853, 4.422067616610029]}
store['active_learning_steps'].append({})
store['active_learning_steps'][12]['training']={}
store['active_learning_steps'][12]['training']['epochs']=[]
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.9507596492767334})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.376649856567383})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.42464017868042})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.794351577758789})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.887824773788452})
store['active_learning_steps'][12]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.766977310180664})
store['active_learning_steps'][12]['training']['best_epoch']=3
store['active_learning_steps'][12]['evaluation_metrics']={'accuracy': 0.6328, 'crossentropy': 2.670640625}
store['active_learning_steps'][12]['acquisition']={'indices': [['id', 12758], ['id', 50538], ['id', 37995], ['id', 20894], ['id', 15935]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6476252100882087, 2.883534810370647, 3.7275535731959923, 4.189664456995421, 4.421445185068482]}
store['active_learning_steps'].append({})
store['active_learning_steps'][13]['training']={}
store['active_learning_steps'][13]['training']['epochs']=[]
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.998140811920166})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.4320292472839355})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.5781149864196777})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.6318492889404297})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.9821600914001465})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 3.247342109680176})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.8892874717712402})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.0611910820007324})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.1323745250701904})
store['active_learning_steps'][13]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.970275402069092})
store['active_learning_steps'][13]['training']['best_epoch']=7
store['active_learning_steps'][13]['evaluation_metrics']={'accuracy': 0.6168, 'crossentropy': 3.361349609375}
store['active_learning_steps'][13]['acquisition']={'indices': [['id', 13250], ['id', 23453], ['id', 11739], ['id', 40853], ['id', 30416]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.59924240038914, 2.946522543153002, 3.7921629358974727, 4.258097377254304, 4.464149575260815]}
store['active_learning_steps'].append({})
store['active_learning_steps'][14]['training']={}
store['active_learning_steps'][14]['training']['epochs']=[]
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.847198724746704})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.546463966369629})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.830280303955078})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.8262901306152344})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 2.9357714653015137})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.2328920364379883})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.2664899826049805})
store['active_learning_steps'][14]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.2001945972442627})
store['active_learning_steps'][14]['training']['best_epoch']=5
store['active_learning_steps'][14]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 3.12937734375}
store['active_learning_steps'][14]['acquisition']={'indices': [['id', 35791], ['id', 1987], ['id', 23121], ['id', 31779], ['id', 17728]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4959033798875545, 2.7436451050209136, 3.6654012018943094, 4.169084160202715, 4.415208310943434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][15]['training']={}
store['active_learning_steps'][15]['training']['epochs']=[]
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 1.8855195045471191})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.3083722591400146})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.6342482566833496})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.8268260955810547})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.1072912216186523})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.9787003993988037})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.315502643585205})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 3.320861577987671})
store['active_learning_steps'][15]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.9530582427978516})
store['active_learning_steps'][15]['training']['best_epoch']=6
store['active_learning_steps'][15]['evaluation_metrics']={'accuracy': 0.6272, 'crossentropy': 3.0892400390625}
store['active_learning_steps'][15]['acquisition']={'indices': [['id', 17510], ['id', 8579], ['id', 48926], ['id', 32489], ['id', 18684]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5643435621940815, 2.7993364126972353, 3.7059513539379605, 4.194046608663033, 4.439361705871427]}
store['active_learning_steps'].append({})
store['active_learning_steps'][16]['training']={}
store['active_learning_steps'][16]['training']['epochs']=[]
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.5986328125, 'crossentropy': 2.064642906188965})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.7295145988464355})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.284882068634033})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.1631412506103516})
store['active_learning_steps'][16]['training']['epochs'].append({'accuracy': 0.6064453125, 'crossentropy': 3.3904037475585938})
store['active_learning_steps'][16]['training']['best_epoch']=2
store['active_learning_steps'][16]['evaluation_metrics']={'accuracy': 0.6033, 'crossentropy': 2.7931779296875}
store['active_learning_steps'][16]['acquisition']={'indices': [['id', 49418], ['id', 11739], ['id', 19869], ['id', 12458], ['id', 54092]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3902638482943734, 2.539214285423566, 3.4069551740576713, 3.930660653121988, 4.226469513320998]}
store['active_learning_steps'].append({})
store['active_learning_steps'][17]['training']={}
store['active_learning_steps'][17]['training']['epochs']=[]
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 2.022106409072876})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 3.0183916091918945})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.111088514328003})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.1999714374542236})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.85977840423584})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3116164207458496})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.087801694869995})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.2147154808044434})
store['active_learning_steps'][17]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.533977508544922})
store['active_learning_steps'][17]['training']['best_epoch']=6
store['active_learning_steps'][17]['evaluation_metrics']={'accuracy': 0.6139, 'crossentropy': 3.448035546875}
store['active_learning_steps'][17]['acquisition']={'indices': [['id', 22960], ['id', 37258], ['id', 10321], ['id', 5316], ['id', 16603]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.5572582552910275, 2.8001583845632148, 3.6749602247166697, 4.1631004300619985, 4.406340010124161]}
store['active_learning_steps'].append({})
store['active_learning_steps'][18]['training']={}
store['active_learning_steps'][18]['training']['epochs']=[]
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.8092427253723145})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.319915533065796})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.7048025131225586})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6533203125, 'crossentropy': 2.7780933380126953})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0233731269836426})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.142770290374756})
store['active_learning_steps'][18]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.0234336853027344})
store['active_learning_steps'][18]['training']['best_epoch']=4
store['active_learning_steps'][18]['evaluation_metrics']={'accuracy': 0.6182, 'crossentropy': 2.8242767578125}
store['active_learning_steps'][18]['acquisition']={'indices': [['id', 14715], ['id', 4380], ['id', 11627], ['id', 32397], ['id', 14147]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5186406779656805, 2.71613337594551, 3.576058046531907, 4.081192405576669, 4.354072496433226]}
store['active_learning_steps'].append({})
store['active_learning_steps'][19]['training']={}
store['active_learning_steps'][19]['training']['epochs']=[]
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 2.1219663619995117})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.623797655105591})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5869140625, 'crossentropy': 3.0669174194335938})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.5830078125, 'crossentropy': 3.163120746612549})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.3367514610290527})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.3062543869018555})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.6025390625, 'crossentropy': 3.4652981758117676})
store['active_learning_steps'][19]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.429391622543335})
store['active_learning_steps'][19]['training']['best_epoch']=5
store['active_learning_steps'][19]['evaluation_metrics']={'accuracy': 0.6142, 'crossentropy': 3.35053984375}
store['active_learning_steps'][19]['acquisition']={'indices': [['id', 37731], ['id', 37621], ['id', 15867], ['id', 10844], ['id', 28500]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6722117893541562, 2.8607064703706238, 3.6816467271033737, 4.167780787370741, 4.40177292594218]}
store['active_learning_steps'].append({})
store['active_learning_steps'][20]['training']={}
store['active_learning_steps'][20]['training']['epochs']=[]
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 2.036774158477783})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.5321807861328125})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.604051351547241})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.9963431358337402})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0612215995788574})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.968440532684326})
store['active_learning_steps'][20]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1129209995269775})
store['active_learning_steps'][20]['training']['best_epoch']=4
store['active_learning_steps'][20]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 3.36719453125}
store['active_learning_steps'][20]['acquisition']={'indices': [['id', 906], ['id', 36578], ['id', 12266], ['id', 20268], ['id', 48926]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4843396759097076, 2.654436399797431, 3.526469082463012, 4.060721255168655, 4.3430942065516]}
store['active_learning_steps'].append({})
store['active_learning_steps'][21]['training']={}
store['active_learning_steps'][21]['training']['epochs']=[]
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 1.628357172012329})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.1553804874420166})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.4649438858032227})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.597684860229492})
store['active_learning_steps'][21]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.643899917602539})
store['active_learning_steps'][21]['training']['best_epoch']=2
store['active_learning_steps'][21]['evaluation_metrics']={'accuracy': 0.6338, 'crossentropy': 2.3485732421875}
store['active_learning_steps'][21]['acquisition']={'indices': [['id', 35158], ['id', 35930], ['id', 28248], ['id', 25840], ['id', 39545]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4797073370950815, 2.7492245162851843, 3.683127765697744, 4.146080796522395, 4.385792474508504]}
store['active_learning_steps'].append({})
store['active_learning_steps'][22]['training']={}
store['active_learning_steps'][22]['training']['epochs']=[]
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.9780319929122925})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.4925777912139893})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.962552547454834})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.1390116214752197})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 2.7711470127105713})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.6103515625, 'crossentropy': 3.363821506500244})
store['active_learning_steps'][22]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.478254556655884})
store['active_learning_steps'][22]['training']['best_epoch']=4
store['active_learning_steps'][22]['evaluation_metrics']={'accuracy': 0.6017, 'crossentropy': 3.284996484375}
store['active_learning_steps'][22]['acquisition']={'indices': [['id', 14715], ['id', 12638], ['id', 24620], ['id', 4080], ['id', 40798]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.587188921304389, 2.7864139863990522, 3.65032246155984, 4.141244317677078, 4.389718996625648]}
store['active_learning_steps'].append({})
store['active_learning_steps'][23]['training']={}
store['active_learning_steps'][23]['training']['epochs']=[]
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8352479934692383})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 2.404813051223755})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.4754738807678223})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.727703809738159})
store['active_learning_steps'][23]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.6946234703063965})
store['active_learning_steps'][23]['training']['best_epoch']=2
store['active_learning_steps'][23]['evaluation_metrics']={'accuracy': 0.6205, 'crossentropy': 2.60174765625}
store['active_learning_steps'][23]['acquisition']={'indices': [['id', 59009], ['id', 59603], ['id', 10308], ['id', 2741], ['id', 39451]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4546758603839716, 2.5782185545088825, 3.414695563154581, 3.9318509497059893, 4.228847407211838]}
store['active_learning_steps'].append({})
store['active_learning_steps'][24]['training']={}
store['active_learning_steps'][24]['training']['epochs']=[]
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.9154767990112305})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.344585418701172})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.656684398651123})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.831911087036133})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.685471534729004})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.883697032928467})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.0828378200531006})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.447977066040039})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.053081512451172})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.16756272315979})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.4035582542419434})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.892327308654785})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.269111156463623})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.600635528564453})
store['active_learning_steps'][24]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.461425304412842})
store['active_learning_steps'][24]['training']['best_epoch']=12
store['active_learning_steps'][24]['evaluation_metrics']={'accuracy': 0.6267, 'crossentropy': 3.4406375}
store['active_learning_steps'][24]['acquisition']={'indices': [['id', 45198], ['id', 17811], ['id', 14129], ['id', 934], ['id', 27105]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.7081552172912389, 2.9641916071978596, 3.7880980893810117, 4.245810199557168, 4.4629005836225195]}
store['active_learning_steps'].append({})
store['active_learning_steps'][25]['training']={}
store['active_learning_steps'][25]['training']['epochs']=[]
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.0049540996551514})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.4139907360076904})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.8272111415863037})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 3.142695903778076})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 3.1791253089904785})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.117701768875122})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.3185369968414307})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 2.9992151260375977})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.2771458625793457})
store['active_learning_steps'][25]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.2182095050811768})
store['active_learning_steps'][25]['training']['best_epoch']=7
store['active_learning_steps'][25]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 3.59822578125}
store['active_learning_steps'][25]['acquisition']={'indices': [['id', 14715], ['id', 12481], ['id', 14756], ['id', 41949], ['id', 25823]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6649352506316868, 2.9838523701250055, 3.8572173752681254, 4.265138656984075, 4.459962746093437]}
store['active_learning_steps'].append({})
store['active_learning_steps'][26]['training']={}
store['active_learning_steps'][26]['training']['epochs']=[]
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.9724889993667603})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.5842254161834717})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 2.7597780227661133})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.8568501472473145})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.5966796875, 'crossentropy': 2.954430103302002})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 3.302570343017578})
store['active_learning_steps'][26]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.4543046951293945})
store['active_learning_steps'][26]['training']['best_epoch']=4
store['active_learning_steps'][26]['evaluation_metrics']={'accuracy': 0.6126, 'crossentropy': 3.0984650390625}
store['active_learning_steps'][26]['acquisition']={'indices': [['id', 25180], ['id', 37613], ['id', 47420], ['id', 34916], ['id', 17129]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6231246289015422, 2.836311542342347, 3.689921563993008, 4.173892898944331, 4.416954991813023]}
store['active_learning_steps'].append({})
store['active_learning_steps'][27]['training']={}
store['active_learning_steps'][27]['training']['epochs']=[]
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 1.9499040842056274})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.3003358840942383})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 2.7523906230926514})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.937279224395752})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.2576904296875})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 2.724069118499756})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.0004220008850098})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.9293110370635986})
store['active_learning_steps'][27]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.1960132122039795})
store['active_learning_steps'][27]['training']['best_epoch']=6
store['active_learning_steps'][27]['evaluation_metrics']={'accuracy': 0.6191, 'crossentropy': 2.88242109375}
store['active_learning_steps'][27]['acquisition']={'indices': [['id', 51350], ['id', 8027], ['id', 39979], ['id', 21700], ['id', 35930]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5246148988071095, 2.747332146328314, 3.625887621492855, 4.130376296601832, 4.38092616640391]}
store['active_learning_steps'].append({})
store['active_learning_steps'][28]['training']={}
store['active_learning_steps'][28]['training']['epochs']=[]
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.045889377593994})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.582080841064453})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.9599695205688477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 3.1005945205688477})
store['active_learning_steps'][28]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9909346103668213})
store['active_learning_steps'][28]['training']['best_epoch']=2
store['active_learning_steps'][28]['evaluation_metrics']={'accuracy': 0.5998, 'crossentropy': 2.754149609375}
store['active_learning_steps'][28]['acquisition']={'indices': [['id', 57292], ['id', 45462], ['id', 35158], ['id', 5790], ['id', 20784]], 'labels': [-1, -1, -1, -1, 5], 'scores': [1.4078025096019822, 2.4847485058504257, 3.337188167141732, 3.873399773828597, 4.200605200294746]}
store['active_learning_steps'].append({})
store['active_learning_steps'][29]['training']={}
store['active_learning_steps'][29]['training']['epochs']=[]
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8461439609527588})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.6483194828033447})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.800633430480957})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.274844169616699})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.9549877643585205})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.951063632965088})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.1566991806030273})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.01395320892334})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.4778242111206055})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.8689165115356445})
store['active_learning_steps'][29]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3862009048461914})
store['active_learning_steps'][29]['training']['best_epoch']=8
store['active_learning_steps'][29]['evaluation_metrics']={'accuracy': 0.6224, 'crossentropy': 3.47558203125}
store['active_learning_steps'][29]['acquisition']={'indices': [['id', 25180], ['id', 43805], ['id', 39655], ['id', 34485], ['id', 2496]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6897442271245087, 2.970486708805534, 3.8170329633314415, 4.269180915862962, 4.475386211294712]}
store['active_learning_steps'].append({})
store['active_learning_steps'][30]['training']={}
store['active_learning_steps'][30]['training']['epochs']=[]
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.65234375, 'crossentropy': 1.6775121688842773})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.27984619140625})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.3025872707366943})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6876955032348633})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.709522247314453})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.684507131576538})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.079423427581787})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.7914583683013916})
store['active_learning_steps'][30]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.790567398071289})
store['active_learning_steps'][30]['training']['best_epoch']=6
store['active_learning_steps'][30]['evaluation_metrics']={'accuracy': 0.6258, 'crossentropy': 2.902315234375}
store['active_learning_steps'][30]['acquisition']={'indices': [['id', 30279], ['id', 27413], ['id', 37040], ['id', 57308], ['id', 32957]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5958621431698594, 2.905079232946342, 3.7806336565751915, 4.225053370826696, 4.439890085191061]}
store['active_learning_steps'].append({})
store['active_learning_steps'][31]['training']={}
store['active_learning_steps'][31]['training']['epochs']=[]
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 1.6978861093521118})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.2752699851989746})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.5795304775238037})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.469069004058838})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.632068157196045})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.621183395385742})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.654296875, 'crossentropy': 2.7188525199890137})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.646484375, 'crossentropy': 2.6744580268859863})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.7825894355773926})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.883885383605957})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.673828125, 'crossentropy': 2.7744524478912354})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 2.8871781826019287})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 2.655074119567871})
store['active_learning_steps'][31]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.2218146324157715})
store['active_learning_steps'][31]['training']['best_epoch']=11
store['active_learning_steps'][31]['evaluation_metrics']={'accuracy': 0.6404, 'crossentropy': 3.1146150390625}
store['active_learning_steps'][31]['acquisition']={'indices': [['id', 5348], ['id', 38216], ['id', 46493], ['id', 55559], ['id', 45056]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.59727724668452, 2.7841058246378436, 3.644878983738769, 4.171303311763076, 4.417309407144489]}
store['active_learning_steps'].append({})
store['active_learning_steps'][32]['training']={}
store['active_learning_steps'][32]['training']['epochs']=[]
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6044921875, 'crossentropy': 2.2009196281433105})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.2984156608581543})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4395663738250732})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.498440742492676})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.888916015625})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.8336119651794434})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.586667537689209})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.9347496032714844})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.107944965362549})
store['active_learning_steps'][32]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0992302894592285})
store['active_learning_steps'][32]['training']['best_epoch']=7
store['active_learning_steps'][32]['evaluation_metrics']={'accuracy': 0.6217, 'crossentropy': 2.833870703125}
store['active_learning_steps'][32]['acquisition']={'indices': [['id', 48536], ['id', 59097], ['id', 15917], ['id', 44039], ['id', 39022]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.593217010302911, 2.8315217677777653, 3.6745106541825034, 4.156245254854214, 4.413512519050358]}
store['active_learning_steps'].append({})
store['active_learning_steps'][33]['training']={}
store['active_learning_steps'][33]['training']['epochs']=[]
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 1.857852578163147})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.634290933609009})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.113412380218506})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.031860828399658})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.968958854675293})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0345866680145264})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.924996852874756})
store['active_learning_steps'][33]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 3.1919989585876465})
store['active_learning_steps'][33]['training']['best_epoch']=5
store['active_learning_steps'][33]['evaluation_metrics']={'accuracy': 0.6301, 'crossentropy': 3.192286328125}
store['active_learning_steps'][33]['acquisition']={'indices': [['id', 42934], ['id', 6434], ['id', 48926], ['id', 54473], ['id', 13951]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6142351490655802, 2.8581949738539167, 3.7274033929204275, 4.1919458198389545, 4.4083832482346725]}
store['active_learning_steps'].append({})
store['active_learning_steps'][34]['training']={}
store['active_learning_steps'][34]['training']['epochs']=[]
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 1.9443687200546265})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.4857330322265625})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 2.6982221603393555})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.962451457977295})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.0339934825897217})
store['active_learning_steps'][34]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.735778570175171})
store['active_learning_steps'][34]['training']['best_epoch']=3
store['active_learning_steps'][34]['evaluation_metrics']={'accuracy': 0.6184, 'crossentropy': 2.7879251953125}
store['active_learning_steps'][34]['acquisition']={'indices': [['id', 37326], ['id', 24223], ['id', 5340], ['id', 21435], ['id', 33010]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.532648620053732, 2.6591611051392077, 3.5001561662142517, 4.030314646376519, 4.313169208272434]}
store['active_learning_steps'].append({})
store['active_learning_steps'][35]['training']={}
store['active_learning_steps'][35]['training']['epochs']=[]
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8501486778259277})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.357025623321533})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.8447437286376953})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.780074119567871})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.782500743865967})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.938135862350464})
store['active_learning_steps'][35]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.1714558601379395})
store['active_learning_steps'][35]['training']['best_epoch']=4
store['active_learning_steps'][35]['evaluation_metrics']={'accuracy': 0.6155, 'crossentropy': 3.0517216796875}
store['active_learning_steps'][35]['acquisition']={'indices': [['id', 42092], ['id', 25435], ['id', 45535], ['id', 54456], ['id', 9707]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5758754845874305, 2.782022117323022, 3.6157913449586117, 4.128800330211949, 4.385486036671802]}
store['active_learning_steps'].append({})
store['active_learning_steps'][36]['training']={}
store['active_learning_steps'][36]['training']['epochs']=[]
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 1.8984951972961426})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.3714661598205566})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6494140625, 'crossentropy': 2.6180667877197266})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.66015625, 'crossentropy': 2.783926486968994})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.65625, 'crossentropy': 2.9257633686065674})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.669921875, 'crossentropy': 2.7890985012054443})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.847142457962036})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6611328125, 'crossentropy': 3.0404577255249023})
store['active_learning_steps'][36]['training']['epochs'].append({'accuracy': 0.6630859375, 'crossentropy': 2.898169994354248})
store['active_learning_steps'][36]['training']['best_epoch']=6
store['active_learning_steps'][36]['evaluation_metrics']={'accuracy': 0.6358, 'crossentropy': 3.1535841796875}
store['active_learning_steps'][36]['acquisition']={'indices': [['id', 30295], ['id', 36357], ['id', 17973], ['id', 24903], ['id', 22807]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5910380434590787, 2.956597708663829, 3.7806382887192918, 4.237296536695476, 4.440406082830539]}
store['active_learning_steps'].append({})
store['active_learning_steps'][37]['training']={}
store['active_learning_steps'][37]['training']['epochs']=[]
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 2.028425455093384})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 2.2923831939697266})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.425400733947754})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.767911434173584})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.009946584701538})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.075681209564209})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.219796895980835})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 2.893094301223755})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.393617630004883})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.658203125, 'crossentropy': 3.4481401443481445})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.61328125, 'crossentropy': 3.6504411697387695})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.308297634124756})
store['active_learning_steps'][37]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.6432933807373047})
store['active_learning_steps'][37]['training']['best_epoch']=10
store['active_learning_steps'][37]['evaluation_metrics']={'accuracy': 0.6234, 'crossentropy': 3.581947265625}
store['active_learning_steps'][37]['acquisition']={'indices': [['id', 40378], ['id', 28227], ['id', 44903], ['id', 37040], ['id', 37621]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.7228748204175126, 3.0087992711598335, 3.818462831169988, 4.292241368915465, 4.486905494735511]}
store['active_learning_steps'].append({})
store['active_learning_steps'][38]['training']={}
store['active_learning_steps'][38]['training']['epochs']=[]
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 1.9246829748153687})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.270082950592041})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.677429676055908})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7401368618011475})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.9562039375305176})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.33498215675354})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9384384155273438})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.111177921295166})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.369027614593506})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.64453125, 'crossentropy': 3.290843963623047})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 3.4600729942321777})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 3.3123183250427246})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6435546875, 'crossentropy': 3.7389729022979736})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.1795921325683594})
store['active_learning_steps'][38]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 3.5830166339874268})
store['active_learning_steps'][38]['training']['best_epoch']=12
store['active_learning_steps'][38]['evaluation_metrics']={'accuracy': 0.6244, 'crossentropy': 3.622765625}
store['active_learning_steps'][38]['acquisition']={'indices': [['id', 32056], ['id', 10241], ['id', 2073], ['id', 22194], ['id', 14797]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5626170483686617, 2.82093665202036, 3.6810042617513155, 4.167485555310355, 4.413106072268404]}
store['active_learning_steps'].append({})
store['active_learning_steps'][39]['training']={}
store['active_learning_steps'][39]['training']['epochs']=[]
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.8443665504455566})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.3050050735473633})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.706778049468994})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.9794764518737793})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 2.883857250213623})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.0364089012145996})
store['active_learning_steps'][39]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.252216339111328})
store['active_learning_steps'][39]['training']['best_epoch']=4
store['active_learning_steps'][39]['evaluation_metrics']={'accuracy': 0.6085, 'crossentropy': 3.299402734375}
store['active_learning_steps'][39]['acquisition']={'indices': [['id', 39476], ['id', 12604], ['id', 15483], ['id', 31883], ['id', 44737]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5214522474330825, 2.7576787594912826, 3.672338493888601, 4.154674992360347, 4.40743181901653]}
store['active_learning_steps'].append({})
store['active_learning_steps'][40]['training']={}
store['active_learning_steps'][40]['training']['epochs']=[]
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9044586420059204})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.3939321041107178})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.782545566558838})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.9299957752227783})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 2.8907575607299805})
store['active_learning_steps'][40]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 3.5403618812561035})
store['active_learning_steps'][40]['training']['best_epoch']=3
store['active_learning_steps'][40]['evaluation_metrics']={'accuracy': 0.6163, 'crossentropy': 2.9072279296875}
store['active_learning_steps'][40]['acquisition']={'indices': [['id', 34275], ['id', 19771], ['id', 36175], ['id', 27355], ['id', 40775]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5501439138487179, 2.668533409815695, 3.515132189160198, 4.03625109251603, 4.307522745149715]}
store['active_learning_steps'].append({})
store['active_learning_steps'][41]['training']={}
store['active_learning_steps'][41]['training']['epochs']=[]
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.869555115699768})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6240234375, 'crossentropy': 2.3739326000213623})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 2.69755482673645})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.638671875, 'crossentropy': 2.8726694583892822})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 3.0830936431884766})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.1598355770111084})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.6416015625, 'crossentropy': 3.07188081741333})
store['active_learning_steps'][41]['training']['epochs'].append({'accuracy': 0.640625, 'crossentropy': 3.180309534072876})
store['active_learning_steps'][41]['training']['best_epoch']=5
store['active_learning_steps'][41]['evaluation_metrics']={'accuracy': 0.6287, 'crossentropy': 3.1595044921875}
store['active_learning_steps'][41]['acquisition']={'indices': [['id', 13914], ['id', 28920], ['id', 59737], ['id', 32459], ['id', 22634]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.66161006385091, 2.89445420333624, 3.781014587569838, 4.2536342149791775, 4.47848133076522]}
store['active_learning_steps'].append({})
store['active_learning_steps'][42]['training']={}
store['active_learning_steps'][42]['training']['epochs']=[]
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 2.009467363357544})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.501560688018799})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.7947983741760254})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 2.996506690979004})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.611328125, 'crossentropy': 3.533982038497925})
store['active_learning_steps'][42]['training']['epochs'].append({'accuracy': 0.609375, 'crossentropy': 3.3770642280578613})
store['active_learning_steps'][42]['training']['best_epoch']=3
store['active_learning_steps'][42]['evaluation_metrics']={'accuracy': 0.6075, 'crossentropy': 2.933776171875}
store['active_learning_steps'][42]['acquisition']={'indices': [['id', 969], ['id', 21934], ['id', 25683], ['id', 58182], ['id', 38539]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4752329310448746, 2.6848621602427194, 3.5474218128242843, 4.070214567862701, 4.356692686088584]}
store['active_learning_steps'].append({})
store['active_learning_steps'][43]['training']={}
store['active_learning_steps'][43]['training']['epochs']=[]
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6162109375, 'crossentropy': 1.8783924579620361})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 2.333949327468872})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.6408658027648926})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.6706089973449707})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 2.755821466445923})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.929957866668701})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 2.9031598567962646})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 3.0019922256469727})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.3311409950256348})
store['active_learning_steps'][43]['training']['epochs'].append({'accuracy': 0.6318359375, 'crossentropy': 3.061455249786377})
store['active_learning_steps'][43]['training']['best_epoch']=7
store['active_learning_steps'][43]['evaluation_metrics']={'accuracy': 0.6256, 'crossentropy': 3.0112548828125}
store['active_learning_steps'][43]['acquisition']={'indices': [['id', 24866], ['id', 33077], ['id', 18135], ['id', 16210], ['id', 20124]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5946393296750725, 2.9070122040136184, 3.7824661716529153, 4.22308922404787, 4.442680037181087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][44]['training']={}
store['active_learning_steps'][44]['training']['epochs']=[]
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 1.816502332687378})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.0764665603637695})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.6154942512512207})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6484375, 'crossentropy': 2.5675039291381836})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6650390625, 'crossentropy': 2.630044460296631})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6572265625, 'crossentropy': 2.8384010791778564})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.8955078125})
store['active_learning_steps'][44]['training']['epochs'].append({'accuracy': 0.6552734375, 'crossentropy': 2.4681687355041504})
store['active_learning_steps'][44]['training']['best_epoch']=5
store['active_learning_steps'][44]['evaluation_metrics']={'accuracy': 0.6422, 'crossentropy': 2.997080078125}
store['active_learning_steps'][44]['acquisition']={'indices': [['id', 59333], ['id', 49418], ['id', 8363], ['id', 37322], ['id', 37613]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.655498916970826, 2.982944647264776, 3.8069946465804474, 4.247361361761033, 4.450346728375626]}
store['active_learning_steps'].append({})
store['active_learning_steps'][45]['training']={}
store['active_learning_steps'][45]['training']['epochs']=[]
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.9547860622406006})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.248807430267334})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6337890625, 'crossentropy': 2.6501221656799316})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 2.88948392868042})
store['active_learning_steps'][45]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.127845287322998})
store['active_learning_steps'][45]['training']['best_epoch']=2
store['active_learning_steps'][45]['evaluation_metrics']={'accuracy': 0.6215, 'crossentropy': 2.4921466796875}
store['active_learning_steps'][45]['acquisition']={'indices': [['id', 30421], ['id', 48926], ['id', 39545], ['id', 44332], ['id', 45048]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.4608231417931394, 2.607640962745479, 3.423172878039635, 3.975267558201857, 4.255513396891484]}
store['active_learning_steps'].append({})
store['active_learning_steps'][46]['training']={}
store['active_learning_steps'][46]['training']['epochs']=[]
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6220703125, 'crossentropy': 1.8864085674285889})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.4893460273742676})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 2.671468734741211})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.0613670349121094})
store['active_learning_steps'][46]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 3.1689412593841553})
store['active_learning_steps'][46]['training']['best_epoch']=2
store['active_learning_steps'][46]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 2.5933810546875}
store['active_learning_steps'][46]['acquisition']={'indices': [['id', 55545], ['id', 23421], ['id', 3219], ['id', 16911], ['id', 8964]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.3973716647496488, 2.5291747029990743, 3.42204564454876, 3.984350434910957, 4.282583938180087]}
store['active_learning_steps'].append({})
store['active_learning_steps'][47]['training']={}
store['active_learning_steps'][47]['training']['epochs']=[]
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 1.91611909866333})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6171875, 'crossentropy': 2.4251914024353027})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.5399975776672363})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6474609375, 'crossentropy': 2.772981643676758})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.650390625, 'crossentropy': 2.7338290214538574})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.107990264892578})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.0891990661621094})
store['active_learning_steps'][47]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0521433353424072})
store['active_learning_steps'][47]['training']['best_epoch']=5
store['active_learning_steps'][47]['evaluation_metrics']={'accuracy': 0.6303, 'crossentropy': 2.8637548828125}
store['active_learning_steps'][47]['acquisition']={'indices': [['id', 26850], ['id', 55591], ['id', 16007], ['id', 16796], ['id', 59656]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5375923056911605, 2.7506976696405836, 3.6045091557302307, 4.128817399266837, 4.391455668520466]}
store['active_learning_steps'].append({})
store['active_learning_steps'][48]['training']={}
store['active_learning_steps'][48]['training']['epochs']=[]
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.599609375, 'crossentropy': 1.9988901615142822})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.4325621128082275})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 2.775081157684326})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 3.319091320037842})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.2613115310668945})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.032867431640625})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3059606552124023})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 3.093071460723877})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6181640625, 'crossentropy': 3.430887460708618})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.62890625, 'crossentropy': 3.4386467933654785})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.6303205490112305})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.6298828125, 'crossentropy': 3.3747825622558594})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 3.304354667663574})
store['active_learning_steps'][48]['training']['epochs'].append({'accuracy': 0.625, 'crossentropy': 3.36106538772583})
store['active_learning_steps'][48]['training']['best_epoch']=11
store['active_learning_steps'][48]['evaluation_metrics']={'accuracy': 0.6212, 'crossentropy': 3.956248828125}
store['active_learning_steps'][48]['acquisition']={'indices': [['id', 25908], ['id', 42198], ['id', 55629], ['id', 26427], ['id', 46219]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6460109636398563, 2.9144229476968646, 3.8115024458729536, 4.290376501163827, 4.490571288117903]}
store['active_learning_steps'].append({})
store['active_learning_steps'][49]['training']={}
store['active_learning_steps'][49]['training']['epochs']=[]
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.9440826177597046})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 2.4022932052612305})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 2.7941527366638184})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.630859375, 'crossentropy': 2.928603172302246})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6123046875, 'crossentropy': 3.2575631141662598})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.099795341491699})
store['active_learning_steps'][49]['training']['epochs'].append({'accuracy': 0.62109375, 'crossentropy': 3.1374425888061523})
store['active_learning_steps'][49]['training']['best_epoch']=4
store['active_learning_steps'][49]['evaluation_metrics']={'accuracy': 0.6091, 'crossentropy': 3.0437650390625}
store['active_learning_steps'][49]['acquisition']={'indices': [['id', 43878], ['id', 30287], ['id', 56399], ['id', 4832], ['id', 52956]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.523181937681465, 2.820493582702406, 3.693977623010003, 4.184363749886039, 4.4171638482928515]}
store['active_learning_steps'].append({})
store['active_learning_steps'][50]['training']={}
store['active_learning_steps'][50]['training']['epochs']=[]
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 1.8090708255767822})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.486992835998535})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.0560624599456787})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 2.999767780303955})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.0937814712524414})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.6328125, 'crossentropy': 3.3603386878967285})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.623046875, 'crossentropy': 3.0913913249969482})
store['active_learning_steps'][50]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.0688562393188477})
store['active_learning_steps'][50]['training']['best_epoch']=5
store['active_learning_steps'][50]['evaluation_metrics']={'accuracy': 0.6218, 'crossentropy': 3.264350390625}
store['active_learning_steps'][50]['acquisition']={'indices': [['id', 29132], ['id', 9118], ['id', 37777], ['id', 38365], ['id', 38506]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6640400338355255, 2.883007990442678, 3.7413333323613234, 4.218354645158909, 4.448656692725222]}
store['active_learning_steps'].append({})
store['active_learning_steps'][51]['training']={}
store['active_learning_steps'][51]['training']['epochs']=[]
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.5927734375, 'crossentropy': 1.9399447441101074})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6015625, 'crossentropy': 2.771299362182617})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.619140625, 'crossentropy': 2.6491785049438477})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6083984375, 'crossentropy': 3.128478527069092})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.607421875, 'crossentropy': 3.119293689727783})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 3.4539215564727783})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.60546875, 'crossentropy': 3.3580427169799805})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.615234375, 'crossentropy': 3.332040309906006})
store['active_learning_steps'][51]['training']['epochs'].append({'accuracy': 0.6142578125, 'crossentropy': 3.427356719970703})
store['active_learning_steps'][51]['training']['best_epoch']=6
store['active_learning_steps'][51]['evaluation_metrics']={'accuracy': 0.6096, 'crossentropy': 3.489591796875}
store['active_learning_steps'][51]['acquisition']={'indices': [['id', 14715], ['id', 1266], ['id', 6605], ['id', 10860], ['id', 6869]], 'labels': [-1, -1, -1, 8, -1], 'scores': [1.5934900670191814, 2.856169753252776, 3.728568560033465, 4.208060049365107, 4.430003988911847]}
store['active_learning_steps'].append({})
store['active_learning_steps'][52]['training']={}
store['active_learning_steps'][52]['training']['epochs']=[]
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6201171875, 'crossentropy': 1.795682668685913})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.0357108116149902})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.8361005783081055})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.634765625, 'crossentropy': 2.7009267807006836})
store['active_learning_steps'][52]['training']['epochs'].append({'accuracy': 0.6513671875, 'crossentropy': 2.7790329456329346})
store['active_learning_steps'][52]['training']['best_epoch']=2
store['active_learning_steps'][52]['evaluation_metrics']={'accuracy': 0.63, 'crossentropy': 2.4032583984375}
store['active_learning_steps'][52]['acquisition']={'indices': [['id', 29132], ['id', 43513], ['id', 50538], ['id', 8584], ['id', 31220]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.6283195351256858, 2.788319177400695, 3.6406082595765845, 4.113336404787292, 4.355395802923201]}
store['active_learning_steps'].append({})
store['active_learning_steps'][53]['training']={}
store['active_learning_steps'][53]['training']['epochs']=[]
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.59375, 'crossentropy': 1.7455897331237793})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6357421875, 'crossentropy': 2.3239893913269043})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 2.6770272254943848})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.739319324493408})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6279296875, 'crossentropy': 3.1174230575561523})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.6396484375, 'crossentropy': 3.299492120742798})
store['active_learning_steps'][53]['training']['epochs'].append({'accuracy': 0.63671875, 'crossentropy': 3.3667163848876953})
store['active_learning_steps'][53]['training']['best_epoch']=4
store['active_learning_steps'][53]['evaluation_metrics']={'accuracy': 0.6207, 'crossentropy': 3.1306376953125}
store['active_learning_steps'][53]['acquisition']={'indices': [['id', 17626], ['id', 8617], ['id', 56286], ['id', 39118], ['id', 23421]], 'labels': [-1, -1, -1, -1, -1], 'scores': [1.5412337783889396, 2.7499070716306764, 3.6075214402647635, 4.1103298260490355, 4.3609303668747605]}
store['active_learning_steps'].append({})
store['active_learning_steps'][54]['training']={}
store['active_learning_steps'][54]['training']['epochs']=[]
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6259765625, 'crossentropy': 1.8311784267425537})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.626953125, 'crossentropy': 2.4756264686584473})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.5116286277770996})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6455078125, 'crossentropy': 2.5883371829986572})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.7806224822998047})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.6376953125, 'crossentropy': 3.141129970550537})
store['active_learning_steps'][54]['training']['epochs'].append({'accuracy': 0.642578125, 'crossentropy': 2.9598803520202637})
store['active_learning_steps'][54]['training']['best_epoch']=4
store['active_learning_steps'][54]['evaluation_metrics']={'accuracy': 0.6335, 'crossentropy': 2.77058984375}
